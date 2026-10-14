# Customer Churn Data Cleaning Report

## Scope and source

- Source: `data/raw/Telco-Customer-Churn.csv` (read only).
- Cleaned output: `data/cleaned/telco_churn_cleaned.csv`.
- Structured quality output: `data/cleaned/data_quality_report.csv`.
- Script uses paths relative to its own project location, so it can be run from the project root or another working directory.
- Source SHA-256 before and after processing: `88be4b93fbe0cc83421af1c503794c97c342eca914c1576db7c276e61d61358a` (unchanged).

## Row and column counts

| Dataset | Rows | Columns |
|---|---|---|
| Original | 7043 | 21 |
| Cleaned | 7043 | 21 |

No records were removed. Column names and order were preserved.

## Data types before and after

| Column | Before | After |
|---|---|---|
| customerID | string | string |
| gender | str | string |
| SeniorCitizen | int64 | Int64 |
| Partner | str | string |
| Dependents | str | string |
| tenure | int64 | Int64 |
| PhoneService | str | string |
| MultipleLines | str | string |
| InternetService | str | string |
| OnlineSecurity | str | string |
| OnlineBackup | str | string |
| DeviceProtection | str | string |
| TechSupport | str | string |
| StreamingTV | str | string |
| StreamingMovies | str | string |
| Contract | str | string |
| PaperlessBilling | str | string |
| PaymentMethod | str | string |
| MonthlyCharges | float64 | float64 |
| TotalCharges | string | float64 |
| Churn | str | string |

## Missing values before and after

### Before

| Column | Missing |
|---|---|
| customerID | 0 |
| gender | 0 |
| SeniorCitizen | 0 |
| Partner | 0 |
| Dependents | 0 |
| tenure | 0 |
| PhoneService | 0 |
| MultipleLines | 0 |
| InternetService | 0 |
| OnlineSecurity | 0 |
| OnlineBackup | 0 |
| DeviceProtection | 0 |
| TechSupport | 0 |
| StreamingTV | 0 |
| StreamingMovies | 0 |
| Contract | 0 |
| PaperlessBilling | 0 |
| PaymentMethod | 0 |
| MonthlyCharges | 0 |
| TotalCharges | 0 |
| Churn | 0 |

### After

| Column | Missing |
|---|---|
| customerID | 0 |
| gender | 0 |
| SeniorCitizen | 0 |
| Partner | 0 |
| Dependents | 0 |
| tenure | 0 |
| PhoneService | 0 |
| MultipleLines | 0 |
| InternetService | 0 |
| OnlineSecurity | 0 |
| OnlineBackup | 0 |
| DeviceProtection | 0 |
| TechSupport | 0 |
| StreamingTV | 0 |
| StreamingMovies | 0 |
| Contract | 0 |
| PaperlessBilling | 0 |
| PaymentMethod | 0 |
| MonthlyCharges | 0 |
| TotalCharges | 11 |
| Churn | 0 |

## Duplicate and identifier checks

- Duplicate full rows before: **0**; after: **0**.
- Duplicate customer ID occurrences before: **0**; after: **0**.
- Missing customer IDs before: **0**; after: **0**.
- No records were dropped or deduplicated.

## Numeric validation

| Check | Failure count | Status |
|---|---|---|
| tenure_non_numeric_or_missing | 0 | PASS |
| tenure_negative | 0 | PASS |
| tenure_non_integer | 0 | PASS |
| monthly_charges_non_numeric_or_missing | 0 | PASS |
| monthly_charges_negative | 0 | PASS |
| total_charges_unconvertible_nonblank | 0 | PASS |
| total_charges_negative | 0 | PASS |
| senior_citizen_non_numeric_or_missing | 0 | PASS |
| senior_citizen_outside_0_1 | 0 | PASS |
| MonthlyCharges_non_finite | 0 | PASS |
| TotalCharges_non_finite | 0 | PASS |

`tenure` was checked for numeric, integer, and nonnegative values. `MonthlyCharges` and present `TotalCharges` values were checked for numeric and nonnegative values. `SeniorCitizen` was checked against {0, 1}. Invalid values, if any, are retained and reported.

## TotalCharges conversion

- Blank or whitespace-only source strings converted to missing values: **11**.
- Nonblank values successfully converted to numeric: **7032**.
- Nonblank values that failed conversion: **0**.
- Failed nonblank examples: `[]`.
- Negative converted values: **0**.
- Missing values were retained; no charge was imputed and no customer was deleted.

## Zero-tenure records

- Records where `tenure == 0`: **11**.
- Blank `TotalCharges` among zero-tenure records: **11**.
- Blank `TotalCharges` among nonzero-tenure records: **0**.

| customerID | tenure | TotalCharges | MonthlyCharges | Churn |
|---|---|---|---|---|
| 4472-LVYGI | 0 | None | 52.55 | No |
| 3115-CZMZD | 0 | None | 20.25 | No |
| 5709-LVOEQ | 0 | None | 80.85 | No |
| 4367-NUYAO | 0 | None | 25.75 | No |
| 1371-DWPAZ | 0 | None | 56.05 | No |
| 7644-OMVMY | 0 | None | 19.85 | No |
| 3213-VVOLG | 0 | None | 25.35 | No |
| 2520-SGTTA | 0 | None | 20.0 | No |
| 2923-ARZLG | 0 | None | 19.7 | No |
| 4075-WKNIU | 0 | None | 73.35 | No |
| 2775-SEFEE | 0 | None | 61.9 | No |

## Categorical validation

Allowed category sets were explicitly defined for the listed Telco fields, including `No phone service` and `No internet service`. Those meaningful values were preserved.

| Column | Observed values and counts | Unexpected values |
|---|---|---|
| gender | Male (3555), Female (3488) | None |
| Partner | No (3641), Yes (3402) | None |
| Dependents | No (4933), Yes (2110) | None |
| PhoneService | Yes (6361), No (682) | None |
| MultipleLines | No (3390), Yes (2971), No phone service (682) | None |
| InternetService | Fiber optic (3096), DSL (2421), No (1526) | None |
| OnlineSecurity | No (3498), Yes (2019), No internet service (1526) | None |
| OnlineBackup | No (3088), Yes (2429), No internet service (1526) | None |
| DeviceProtection | No (3095), Yes (2422), No internet service (1526) | None |
| TechSupport | No (3473), Yes (2044), No internet service (1526) | None |
| StreamingTV | No (2810), Yes (2707), No internet service (1526) | None |
| StreamingMovies | No (2785), Yes (2732), No internet service (1526) | None |
| Contract | Month-to-month (3875), Two year (1695), One year (1473) | None |
| PaperlessBilling | Yes (4171), No (2872) | None |
| PaymentMethod | Electronic check (2365), Mailed check (1612), Bank transfer (automatic) (1544), Credit card (automatic) (1522) | None |
| Churn | No (5174), Yes (1869) | None |

Whitespace trimmed from categorical columns (and customerID as a text identifier): {"Churn": 0, "Contract": 0, "Dependents": 0, "DeviceProtection": 0, "InternetService": 0, "MultipleLines": 0, "OnlineBackup": 0, "OnlineSecurity": 0, "PaperlessBilling": 0, "Partner": 0, "PaymentMethod": 0, "PhoneService": 0, "StreamingMovies": 0, "StreamingTV": 0, "TechSupport": 0, "customerID": 0, "gender": 0}.

## Cleaning decisions

1. Loaded `customerID` and `TotalCharges` as text at input to preserve their source representation for validation.
2. Confirmed the complete expected column schema and order; the script stops with an error if it differs.
3. Trimmed leading/trailing whitespace in categorical text and customer identifiers, preserving category labels and identifiers as text.
4. Converted blank `TotalCharges` strings to missing values; checked all nonblank strings explicitly with `pandas.to_numeric(errors='coerce')` and recorded failures.
5. Converted `tenure` and `SeniorCitizen` to nullable integer types when tenure values were integral; converted `MonthlyCharges` and `TotalCharges` to numeric types.
6. Kept all rows, left missing `TotalCharges` unfilled, left `Churn` as the Yes/No target, and did not use `Churn` for any imputation.

## Unresolved data-quality issues

- 11 `TotalCharges` values remain missing because source values were blank/whitespace-only; they were retained, not imputed or deleted.

## Readiness

The output is structurally suitable to begin EDA with the unresolved missing `TotalCharges` values kept explicit. Review those cases and any failures listed above before model training; this report does not claim the dataset is fully clean.
