# Raw Data Inspection Report

## Scope and source
- Source: `data/raw/Telco-Customer-Churn.csv` (read only; no source changes made).
- Inspected with Python and Pandas. `TotalCharges` was retained as text for explicit blank and conversion checks.
- Shape: **7,043 rows × 21 columns**.
- Duplicate full rows: **0**.

## Columns and inferred data types
| Column | Pandas dtype | Non-null | Missing | Distinct non-null |
|---|---:|---:|---:|---:|
| customerID | str | 7,043 | 0 | 7,043 |
| gender | str | 7,043 | 0 | 2 |
| SeniorCitizen | int64 | 7,043 | 0 | 2 |
| Partner | str | 7,043 | 0 | 2 |
| Dependents | str | 7,043 | 0 | 2 |
| tenure | int64 | 7,043 | 0 | 73 |
| PhoneService | str | 7,043 | 0 | 2 |
| MultipleLines | str | 7,043 | 0 | 3 |
| InternetService | str | 7,043 | 0 | 3 |
| OnlineSecurity | str | 7,043 | 0 | 3 |
| OnlineBackup | str | 7,043 | 0 | 3 |
| DeviceProtection | str | 7,043 | 0 | 3 |
| TechSupport | str | 7,043 | 0 | 3 |
| StreamingTV | str | 7,043 | 0 | 3 |
| StreamingMovies | str | 7,043 | 0 | 3 |
| Contract | str | 7,043 | 0 | 3 |
| PaperlessBilling | str | 7,043 | 0 | 2 |
| PaymentMethod | str | 7,043 | 0 | 4 |
| MonthlyCharges | float64 | 7,043 | 0 | 1,585 |
| TotalCharges | string | 7,043 | 0 | 6,531 |
| Churn | str | 7,043 | 0 | 2 |

## First five rows
```text
customerID gender  SeniorCitizen Partner Dependents  tenure PhoneService    MultipleLines InternetService OnlineSecurity OnlineBackup DeviceProtection TechSupport StreamingTV StreamingMovies       Contract PaperlessBilling             PaymentMethod  MonthlyCharges TotalCharges Churn
7590-VHVEG Female              0     Yes         No       1           No No phone service             DSL             No          Yes               No          No          No              No Month-to-month              Yes          Electronic check           29.85        29.85    No
5575-GNVDE   Male              0      No         No      34          Yes               No             DSL            Yes           No              Yes          No          No              No       One year               No              Mailed check           56.95       1889.5    No
3668-QPYBK   Male              0      No         No       2          Yes               No             DSL            Yes          Yes               No          No          No              No Month-to-month              Yes              Mailed check           53.85       108.15   Yes
7795-CFOCW   Male              0      No         No      45           No No phone service             DSL            Yes           No              Yes         Yes          No              No       One year               No Bank transfer (automatic)           42.30      1840.75    No
9237-HQITU Female              0      No         No       2          Yes               No     Fiber optic             No           No               No          No          No              No Month-to-month              Yes          Electronic check           70.70       151.65   Yes
```

## Missing values
CSV parser missing values by column:
| Column | Missing |
|---|---:|
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

Text empty/whitespace-only values after trimming: `TotalCharges`: 11

## Duplicates and customer IDs
- `customerID`: 7,043 distinct non-null IDs; 0 repeated occurrences beyond first; missing IDs: 0.

## Category values and whitespace
- `customerID`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
- `gender`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `Male`: 3,555; `Female`: 3,488
- `Partner`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 3,641; `Yes`: 3,402
- `Dependents`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 4,933; `Yes`: 2,110
- `PhoneService`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `Yes`: 6,361; `No`: 682
- `MultipleLines`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 3,390; `Yes`: 2,971; `No phone service`: 682
- `InternetService`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `Fiber optic`: 3,096; `DSL`: 2,421; `No`: 1,526
- `OnlineSecurity`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 3,498; `Yes`: 2,019; `No internet service`: 1,526
- `OnlineBackup`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 3,088; `Yes`: 2,429; `No internet service`: 1,526
- `DeviceProtection`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 3,095; `Yes`: 2,422; `No internet service`: 1,526
- `TechSupport`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 3,473; `Yes`: 2,044; `No internet service`: 1,526
- `StreamingTV`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 2,810; `Yes`: 2,707; `No internet service`: 1,526
- `StreamingMovies`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 2,785; `Yes`: 2,732; `No internet service`: 1,526
- `Contract`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `Month-to-month`: 3,875; `Two year`: 1,695; `One year`: 1,473
- `PaperlessBilling`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `Yes`: 4,171; `No`: 2,872
- `PaymentMethod`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `Electronic check`: 2,365; `Mailed check`: 1,612; `Bank transfer (automatic)`: 1,544; `Credit card (automatic)`: 1,522
- `TotalCharges`: leading-space values 11; trailing-space values 11; values changed by trimming either end 11.
- `Churn`: leading-space values 0; trailing-space values 0; values changed by trimming either end 0.
  - Values/counts: `No`: 5,174; `Yes`: 1,869
- High-cardinality fields (including identifiers and charge amounts) are not expanded into value/count lists; their distinct counts are in the schema table.

## Numeric columns and ranges
| Column | Min | Max | Mean | Integer-valued? |
|---|---:|---:|---:|---|
| SeniorCitizen | 0 | 1 | 0.1621 | yes |
| tenure | 0 | 72 | 32.3711 | yes |
| MonthlyCharges | 18.25 | 118.75 | 64.7617 | no |
- `SeniorCitizen`: no invalid values under expected 0/1 indicator domain.
- `tenure`: no negative values or values above 120 months.
- `MonthlyCharges`: no negative values.

## Total charges conversion check
- Blank/whitespace-only strings: **11**.
- Nonblank values that cannot convert to numeric: **0**.
- Converted numeric values: 7,032; min 18.8; max 8684.8.
- Blank-string row indices (zero-based): 488, 753, 936, 1082, 1340, 3331, 3826, 4380, 5218, 6670, 6754.

## Churn target
| Value | Count |
|---|---:|
| No | 5,174 |
| Yes | 1,869 |

## Type conversion candidates
- `TotalCharges`: text but represents a charge; convert after explicitly treating blank strings as missing and checking conversion failures.
- `SeniorCitizen`: integer 0/1 indicator; consider boolean or categorical representation for labels.
- Categorical text fields: `gender`, `Partner`, `Dependents`, `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`, `PaperlessBilling`, `PaymentMethod`, `Churn`.
- `customerID`: keep as text/string identifier, not a numeric measure.
- `tenure`: integer months; retain integer type.

## Potential target leakage
- No explicit post-churn outcome, cancellation date, or retention-action result field appears in the observed schema. `Churn` is the target and must not be used as a predictor.
- `TotalCharges` is cumulative and closely related to `tenure` and `MonthlyCharges`. It is usable only if available at the prediction date; define the prediction time and check for values accumulated after it. This is a potential timing/proxy risk, not confirmed leakage from the schema alone.
- Service, contract, billing, payment, and tenure fields are not inherently leakage based on names; confirm they were captured as of the scoring date. The CSV alone does not establish recording times.

## Findings and recommended next cleaning steps
- 7,043 records, 21 columns, 0 duplicate full rows.
- `customerID` has 0 repeated occurrences; no ID-based removal is indicated by this check.
- Convert `TotalCharges` to numeric while handling 11 blank string(s) explicitly; 0 nonblank conversion failures found.
- Review the listed categorical domains and whitespace counts; normalize only if needed.
- Validate the numeric domains and document intentional special values before changes.
- Define the prediction snapshot and feature cutoff; exclude `Churn` from predictors and assess `TotalCharges` against that cutoff.
- Preserve the raw CSV; write cleaned output and a cleaning log to `data/cleaned/` in a later step.

## Reproducibility note
All source paths are relative to the project root. Findings describe the CSV as currently stored; the raw file was not modified.
