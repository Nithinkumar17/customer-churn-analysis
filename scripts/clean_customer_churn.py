"""Clean and validate the Telco Customer Churn source dataset.

Run from the project root with:
    python scripts/clean_customer_churn.py

The raw CSV is read only. Outputs are written under data/cleaned/ and reports/.
"""

from __future__ import annotations

from pathlib import Path
import csv
import hashlib
import json
import math
import os
import tempfile

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "Telco-Customer-Churn.csv"
CLEAN_DIR = PROJECT_ROOT / "data" / "cleaned"
CLEAN_PATH = CLEAN_DIR / "telco_churn_cleaned.csv"
QUALITY_PATH = CLEAN_DIR / "data_quality_report.csv"
REPORT_PATH = PROJECT_ROOT / "reports" / "data_cleaning_report.md"

EXPECTED_COLUMNS = [
    "customerID", "gender", "SeniorCitizen", "Partner", "Dependents",
    "tenure", "PhoneService", "MultipleLines", "InternetService",
    "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport",
    "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling",
    "PaymentMethod", "MonthlyCharges", "TotalCharges", "Churn",
]
CATEGORICAL_DOMAINS = {
    "gender": {"Female", "Male"},
    "Partner": {"Yes", "No"},
    "Dependents": {"Yes", "No"},
    "PhoneService": {"Yes", "No"},
    "MultipleLines": {"Yes", "No", "No phone service"},
    "InternetService": {"DSL", "Fiber optic", "No"},
    "OnlineSecurity": {"Yes", "No", "No internet service"},
    "OnlineBackup": {"Yes", "No", "No internet service"},
    "DeviceProtection": {"Yes", "No", "No internet service"},
    "TechSupport": {"Yes", "No", "No internet service"},
    "StreamingTV": {"Yes", "No", "No internet service"},
    "StreamingMovies": {"Yes", "No", "No internet service"},
    "Contract": {"Month-to-month", "One year", "Two year"},
    "PaperlessBilling": {"Yes", "No"},
    "PaymentMethod": {
        "Electronic check", "Mailed check", "Bank transfer (automatic)",
        "Credit card (automatic)",
    },
    "Churn": {"Yes", "No"},
}
CATEGORICAL_COLUMNS = list(CATEGORICAL_DOMAINS)
NUMERIC_COLUMNS = ["tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen"]


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    def cell(value: object) -> str:
        return str(value).replace("|", "\\|").replace("\n", " ")

    output = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    output.extend("| " + " | ".join(cell(value) for value in row) + " |" for row in rows)
    return "\n".join(output)


def safe_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, default=str, sort_keys=True)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if not RAW_PATH.is_file():
        raise FileNotFoundError(f"Required source CSV not found: {RAW_PATH}")

    raw_hash_before = sha256(RAW_PATH)
    raw = pd.read_csv(RAW_PATH, dtype={"customerID": "string", "TotalCharges": "string"})
    columns_before = list(raw.columns)
    if columns_before != EXPECTED_COLUMNS:
        missing = [column for column in EXPECTED_COLUMNS if column not in columns_before]
        unexpected = [column for column in columns_before if column not in EXPECTED_COLUMNS]
        raise ValueError(
            "Source schema does not match expected Telco schema/order. "
            f"Missing columns: {missing}; unexpected columns: {unexpected}; "
            f"actual order: {columns_before}"
        )

    dtypes_before = {column: str(dtype) for column, dtype in raw.dtypes.items()}
    missing_before = {column: int(count) for column, count in raw.isna().sum().items()}
    duplicate_rows_before = int(raw.duplicated().sum())
    duplicate_ids_before = int(raw["customerID"].duplicated(keep="first").sum())
    missing_ids_before = int(raw["customerID"].isna().sum())

    cleaned = raw.copy(deep=True)
    trim_counts: dict[str, int] = {}
    for column in CATEGORICAL_COLUMNS:
        original = cleaned[column].astype("string")
        trimmed = original.str.strip()
        trim_counts[column] = int((original.notna() & original.ne(trimmed)).sum())
        cleaned[column] = trimmed
    ids_original = cleaned["customerID"]
    ids_trimmed = ids_original.str.strip()
    trim_counts["customerID"] = int((ids_original.notna() & ids_original.ne(ids_trimmed)).sum())
    cleaned["customerID"] = ids_trimmed

    charge_text = cleaned["TotalCharges"].astype("string").str.strip()
    blank_charge_mask = charge_text.isna() | charge_text.eq("")
    nonblank_charge_mask = ~blank_charge_mask
    parsed_charges = pd.to_numeric(charge_text.mask(blank_charge_mask), errors="coerce")
    unconvertible_mask = nonblank_charge_mask & parsed_charges.isna()
    unconvertible_values = cleaned.loc[unconvertible_mask, "TotalCharges"].drop_duplicates().tolist()
    cleaned["TotalCharges"] = parsed_charges.astype("float64")

    # Validate numeric fields explicitly; retain every source row even when a failure exists.
    tenure = pd.to_numeric(cleaned["tenure"], errors="coerce")
    monthly = pd.to_numeric(cleaned["MonthlyCharges"], errors="coerce")
    senior = pd.to_numeric(cleaned["SeniorCitizen"], errors="coerce")
    numeric_failures = {
        "tenure_non_numeric_or_missing": int(tenure.isna().sum()),
        "tenure_negative": int((tenure < 0).sum()),
        "tenure_non_integer": int((tenure.notna() & (tenure % 1 != 0)).sum()),
        "monthly_charges_non_numeric_or_missing": int(monthly.isna().sum()),
        "monthly_charges_negative": int((monthly < 0).sum()),
        "total_charges_unconvertible_nonblank": int(unconvertible_mask.sum()),
        "total_charges_negative": int((cleaned["TotalCharges"] < 0).sum()),
        "senior_citizen_non_numeric_or_missing": int(senior.isna().sum()),
        "senior_citizen_outside_0_1": int((senior.notna() & ~senior.isin([0, 1])).sum()),
    }
    # Tenure should remain an integer column; a source parse/domain issue is reported and
    # will fail conversion explicitly instead of silently truncating a fractional value.
    if numeric_failures["tenure_non_integer"]:
        cleaned["tenure"] = tenure
    else:
        cleaned["tenure"] = tenure.astype("Int64")
    cleaned["MonthlyCharges"] = monthly.astype("float64")
    cleaned["SeniorCitizen"] = senior.astype("Int64")

    zero_tenure = cleaned.loc[
        cleaned["tenure"].eq(0), ["customerID", "tenure", "TotalCharges", "MonthlyCharges", "Churn"]
    ].copy()
    zero_tenure_records = zero_tenure.astype(object).where(pd.notna(zero_tenure), None).to_dict("records")
    blank_charge_zero_tenure = int((blank_charge_mask & cleaned["tenure"].eq(0)).sum())
    blank_charge_nonzero_tenure = int((blank_charge_mask & cleaned["tenure"].ne(0)).sum())

    category_results: dict[str, dict[str, object]] = {}
    for column, allowed in CATEGORICAL_DOMAINS.items():
        actual = set(cleaned[column].dropna().astype(str).unique())
        invalid = sorted(actual - allowed)
        category_results[column] = {
            "distinct_values": sorted(actual),
            "counts": {str(key): int(value) for key, value in cleaned[column].value_counts(dropna=False).items()},
            "unexpected_values": invalid,
            "missing": int(cleaned[column].isna().sum()),
        }

    missing_after = {column: int(count) for column, count in cleaned.isna().sum().items()}
    dtypes_after = {column: str(dtype) for column, dtype in cleaned.dtypes.items()}
    duplicate_rows_after = int(cleaned.duplicated().sum())
    duplicate_ids_after = int(cleaned["customerID"].duplicated(keep="first").sum())
    missing_ids_after = int(cleaned["customerID"].isna().sum())
    # Report non-finite numeric values as validation failures as well.
    for column in ["MonthlyCharges", "TotalCharges"]:
        numeric_values = cleaned[column].dropna().astype(float)
        numeric_failures[f"{column}_non_finite"] = int(sum(not math.isfinite(value) for value in numeric_values))
    raw_hash_after = sha256(RAW_PATH)
    if raw_hash_before != raw_hash_after:
        raise RuntimeError("Safety check failed: raw source hash changed during cleaning.")

    # A quality CSV with one row per validation/summary metric and JSON details.
    quality_rows: list[dict[str, str]] = []

    def metric(name: str, group: str, value: object, status: str = "INFO", details: object = "") -> None:
        quality_rows.append({"metric": name, "group": group, "value": str(value), "status": status, "details": safe_json(details)})

    metric("rows_before", "shape", len(raw)); metric("columns_before", "shape", len(raw.columns))
    metric("rows_after", "shape", len(cleaned)); metric("columns_after", "shape", len(cleaned.columns))
    metric("duplicate_full_rows_before", "duplicates", duplicate_rows_before, "PASS" if duplicate_rows_before == 0 else "REVIEW")
    metric("duplicate_full_rows_after", "duplicates", duplicate_rows_after, "PASS" if duplicate_rows_after == 0 else "REVIEW")
    metric("duplicate_customer_ids_before", "duplicates", duplicate_ids_before, "PASS" if duplicate_ids_before == 0 else "REVIEW")
    metric("duplicate_customer_ids_after", "duplicates", duplicate_ids_after, "PASS" if duplicate_ids_after == 0 else "REVIEW")
    metric("missing_customer_ids_before", "identifiers", missing_ids_before, "PASS" if missing_ids_before == 0 else "REVIEW")
    metric("missing_customer_ids_after", "identifiers", missing_ids_after, "PASS" if missing_ids_after == 0 else "REVIEW")
    metric("total_charges_blank_strings", "TotalCharges", int(blank_charge_mask.sum()), "REVIEW" if blank_charge_mask.any() else "PASS")
    metric("total_charges_converted", "TotalCharges", int(parsed_charges.notna().sum()), "INFO")
    metric("total_charges_unconvertible_nonblank", "TotalCharges", int(unconvertible_mask.sum()), "PASS" if not unconvertible_mask.any() else "FAIL", unconvertible_values)
    metric("zero_tenure_records", "tenure", len(zero_tenure), "INFO", zero_tenure_records)
    metric("blank_total_charges_at_zero_tenure", "TotalCharges", blank_charge_zero_tenure, "INFO")
    metric("blank_total_charges_at_nonzero_tenure", "TotalCharges", blank_charge_nonzero_tenure, "REVIEW" if blank_charge_nonzero_tenure else "PASS")
    for column, count in missing_before.items(): metric(f"missing_before.{column}", "missing", count)
    for column, count in missing_after.items(): metric(f"missing_after.{column}", "missing", count, "REVIEW" if count else "PASS")
    for column, dtype in dtypes_before.items(): metric(f"dtype_before.{column}", "dtypes", dtype)
    for column, dtype in dtypes_after.items(): metric(f"dtype_after.{column}", "dtypes", dtype)
    for check, count in numeric_failures.items(): metric(check, "numeric_validation", count, "PASS" if count == 0 else "FAIL")
    for column, result in category_results.items():
        metric(f"{column}.distinct_values", "categorical_validation", result["distinct_values"])
        metric(f"{column}.value_counts", "categorical_validation", result["counts"])
        metric(f"{column}.unexpected_values", "categorical_validation", result["unexpected_values"], "PASS" if not result["unexpected_values"] else "FAIL")
    metric("trimmed_values_by_column", "cleaning", trim_counts)
    metric("source_sha256_before", "safety", raw_hash_before)
    metric("source_sha256_after", "safety", raw_hash_after, "PASS")

    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write outputs through temporary sibling files and replace atomically.
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", newline="", delete=False, dir=CLEAN_DIR, suffix=".tmp") as temp:
        temp_path = Path(temp.name)
    try:
        cleaned.to_csv(temp_path, index=False, quoting=csv.QUOTE_MINIMAL)
        os.replace(temp_path, CLEAN_PATH)
    finally:
        if temp_path.exists():
            temp_path.unlink()
    pd.DataFrame(quality_rows).to_csv(QUALITY_PATH, index=False)

    original_counts = [[column, count] for column, count in missing_before.items()]
    cleaned_counts = [[column, count] for column, count in missing_after.items()]
    dtype_rows = [[column, dtypes_before[column], dtypes_after[column]] for column in columns_before]
    numeric_rows = [[check, count, "PASS" if count == 0 else "FAIL"] for check, count in numeric_failures.items()]
    category_rows = []
    for column, result in category_results.items():
        category_rows.append([
            column,
            ", ".join(f"{value} ({count})" for value, count in result["counts"].items()),
            ", ".join(result["unexpected_values"]) or "None",
        ])
    zero_table = markdown_table(
        ["customerID", "tenure", "TotalCharges", "MonthlyCharges", "Churn"],
        [[record.get(key) for key in ["customerID", "tenure", "TotalCharges", "MonthlyCharges", "Churn"]] for record in zero_tenure_records],
    ) if zero_tenure_records else "No zero-tenure records."
    remaining = []
    remaining.extend(f"- Numeric validation `{name}`: {count} failure(s)." for name, count in numeric_failures.items() if count)
    remaining.extend(f"- Unexpected `{column}` category values: {result['unexpected_values']}." for column, result in category_results.items() if result["unexpected_values"])
    if blank_charge_nonzero_tenure:
        remaining.append(f"- {blank_charge_nonzero_tenure} blank `TotalCharges` record(s) have nonzero tenure; review these cases before modeling.")
    if missing_ids_after:
        remaining.append(f"- {missing_ids_after} missing customer ID(s).")
    if duplicate_rows_after:
        remaining.append(f"- {duplicate_rows_after} duplicate full row(s).")
    if duplicate_ids_after:
        remaining.append(f"- {duplicate_ids_after} repeated customer ID occurrence(s).")
    if blank_charge_mask.any():
        remaining.append(f"- {int(blank_charge_mask.sum())} `TotalCharges` values remain missing because source values were blank/whitespace-only; they were retained, not imputed or deleted.")
    if not remaining:
        remaining.append("- No validation failures were detected by the checks defined in this script.")

    report = [
        "# Customer Churn Data Cleaning Report", "",
        "## Scope and source", "",
        f"- Source: `{RAW_PATH.relative_to(PROJECT_ROOT).as_posix()}` (read only).",
        f"- Cleaned output: `{CLEAN_PATH.relative_to(PROJECT_ROOT).as_posix()}`.",
        f"- Structured quality output: `{QUALITY_PATH.relative_to(PROJECT_ROOT).as_posix()}`.",
        "- Script uses paths relative to its own project location, so it can be run from the project root or another working directory.",
        f"- Source SHA-256 before and after processing: `{raw_hash_before}` (unchanged).", "",
        "## Row and column counts", "",
        markdown_table(["Dataset", "Rows", "Columns"], [["Original", len(raw), len(raw.columns)], ["Cleaned", len(cleaned), len(cleaned.columns)]]), "",
        "No records were removed. Column names and order were preserved.", "",
        "## Data types before and after", "", markdown_table(["Column", "Before", "After"], dtype_rows), "",
        "## Missing values before and after", "", "### Before", "", markdown_table(["Column", "Missing"], original_counts), "",
        "### After", "", markdown_table(["Column", "Missing"], cleaned_counts), "",
        "## Duplicate and identifier checks", "",
        f"- Duplicate full rows before: **{duplicate_rows_before}**; after: **{duplicate_rows_after}**.",
        f"- Duplicate customer ID occurrences before: **{duplicate_ids_before}**; after: **{duplicate_ids_after}**.",
        f"- Missing customer IDs before: **{missing_ids_before}**; after: **{missing_ids_after}**.",
        "- No records were dropped or deduplicated.", "",
        "## Numeric validation", "", markdown_table(["Check", "Failure count", "Status"], numeric_rows), "",
        "`tenure` was checked for numeric, integer, and nonnegative values. `MonthlyCharges` and present `TotalCharges` values were checked for numeric and nonnegative values. `SeniorCitizen` was checked against {0, 1}. Invalid values, if any, are retained and reported.", "",
        "## TotalCharges conversion", "",
        f"- Blank or whitespace-only source strings converted to missing values: **{int(blank_charge_mask.sum())}**.",
        f"- Nonblank values successfully converted to numeric: **{int(parsed_charges.notna().sum())}**.",
        f"- Nonblank values that failed conversion: **{int(unconvertible_mask.sum())}**.",
        f"- Failed nonblank examples: `{unconvertible_values}`.",
        f"- Negative converted values: **{numeric_failures['total_charges_negative']}**.",
        "- Missing values were retained; no charge was imputed and no customer was deleted.", "",
        "## Zero-tenure records", "",
        f"- Records where `tenure == 0`: **{len(zero_tenure)}**.",
        f"- Blank `TotalCharges` among zero-tenure records: **{blank_charge_zero_tenure}**.",
        f"- Blank `TotalCharges` among nonzero-tenure records: **{blank_charge_nonzero_tenure}**.", "",
        zero_table, "",
        "## Categorical validation", "",
        "Allowed category sets were explicitly defined for the listed Telco fields, including `No phone service` and `No internet service`. Those meaningful values were preserved.", "",
        markdown_table(["Column", "Observed values and counts", "Unexpected values"], category_rows), "",
        "Whitespace trimmed from categorical columns (and customerID as a text identifier): " + safe_json(trim_counts) + ".", "",
        "## Cleaning decisions", "",
        "1. Loaded `customerID` and `TotalCharges` as text at input to preserve their source representation for validation.",
        "2. Confirmed the complete expected column schema and order; the script stops with an error if it differs.",
        "3. Trimmed leading/trailing whitespace in categorical text and customer identifiers, preserving category labels and identifiers as text.",
        "4. Converted blank `TotalCharges` strings to missing values; checked all nonblank strings explicitly with `pandas.to_numeric(errors='coerce')` and recorded failures.",
        "5. Converted `tenure` and `SeniorCitizen` to nullable integer types when tenure values were integral; converted `MonthlyCharges` and `TotalCharges` to numeric types.",
        "6. Kept all rows, left missing `TotalCharges` unfilled, left `Churn` as the Yes/No target, and did not use `Churn` for any imputation.", "",
        "## Unresolved data-quality issues", "", *remaining, "",
        "## Readiness", "",
        ("The output is structurally suitable to begin EDA with the unresolved missing `TotalCharges` values kept explicit. Review those cases and any failures listed above before model training; this report does not claim the dataset is fully clean." if blank_charge_mask.any() or any(numeric_failures.values()) or any(r["unexpected_values"] for r in category_results.values()) else "No issues were detected by the implemented checks; still review the feature timing and domain assumptions before modeling."), "",
    ]
    REPORT_PATH.write_text("\n".join(report), encoding="utf-8")

    # Final verification of generated files, output shape, and immutable input.
    for path in [CLEAN_PATH, QUALITY_PATH, REPORT_PATH]:
        if not path.is_file() or path.stat().st_size == 0:
            raise RuntimeError(f"Expected output missing or empty: {path}")
    reloaded = pd.read_csv(CLEAN_PATH, dtype={"customerID": "string"})
    if reloaded.shape != cleaned.shape or list(reloaded.columns) != EXPECTED_COLUMNS:
        raise RuntimeError("Cleaned output verification failed: unexpected shape or columns.")
    if sha256(RAW_PATH) != raw_hash_before:
        raise RuntimeError("Safety check failed: raw source file changed.")

    print(f"Cleaned dataset: {CLEAN_PATH.relative_to(PROJECT_ROOT).as_posix()}")
    print(f"Quality report: {QUALITY_PATH.relative_to(PROJECT_ROOT).as_posix()}")
    print(f"Cleaning report: {REPORT_PATH.relative_to(PROJECT_ROOT).as_posix()}")
    print(f"Final shape: {reloaded.shape}")
    print("Final dtypes:")
    print(reloaded.dtypes.to_string())
    print("Missing-value counts:")
    print(reloaded.isna().sum().to_string())
    print(f"Duplicate rows: {reloaded.duplicated().sum()}")
    print(f"Duplicate customer IDs: {reloaded['customerID'].duplicated().sum()}")
    print(f"TotalCharges successfully converted: {int(parsed_charges.notna().sum())}")
    print(f"Zero-tenure records: {len(zero_tenure)}")
    failures = sum(numeric_failures.values()) + sum(len(result["unexpected_values"]) for result in category_results.values())
    print(f"Validation failures: {failures}")
    print(f"Raw source unchanged (SHA-256): {raw_hash_before == sha256(RAW_PATH)}")


if __name__ == "__main__":
    main()
