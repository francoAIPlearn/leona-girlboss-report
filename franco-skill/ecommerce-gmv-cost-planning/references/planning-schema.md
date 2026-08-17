# Planning Schema and Formulas

## Core terms

| Field | Definition |
|---|---|
| `platform_target_gmv` | GMV target for the platform whose costs are planned |
| `store_total_gmv` | Sum of all platform GMV targets; never substitute for platform ROI numerator |
| `forecast_full_month_gmv` | Full-month projection from current partial-month actuals when the comparison month is incomplete |
| `full_site_roi` | Platform GMV divided by all included channel expenses |
| `ad_roas` | Attributed ad GMV divided by ad spend; diagnostic, not the full expense constraint |
| `planning_growth` | User-provided business target label |
| `calculated_growth` | `target / comparable_baseline - 1`; use `forecast_full_month_gmv` when comparing a partial month to a full-month target |
| `other` | Residual after explicit category or product targets |

## Required closure equations

```text
store_total_gmv = sum(platform_gmv_targets)
expense_budget = round(costed_platform_gmv / full_site_roi)
full_site_expense_ratio = expense_budget / costed_platform_gmv
sum(category_target_gmv) = costed_platform_gmv
sum(product_target_gmv) = costed_platform_gmv
sum(channel_budgets) = expense_budget
sum(daily_platform_gmv) = monthly_platform_gmv
sum(daily_channel_cost) = monthly_channel_budget
```

Use decimal arithmetic for validation. Apply display rounding only after totals close.

## Channel allocation

Represent priorities as groups because `other` may contain multiple channels. Confirm the final order with the responsible owner before treating it as locked:

```json
"priority_groups": [
  ["px"],
  ["onsite_ads"],
  ["offsite_ads"],
  ["voucher", "affiliate"]
]
```

Validate the sum of each group, not each label independently.

## Daily normalization

For weight-based channels:

```text
daily_budget[d] = monthly_budget 脳 weight[d] / sum(weights)
```

For GMV-linked rates:

```text
raw_cost[d] = daily_gmv[d] 脳 base_rate[d]
daily_budget[d] = monthly_budget 脳 raw_cost[d] / sum(raw_cost)
```

For PX or commission programs:

```text
raw_px[d] = daily_gmv[d] 脳 commission_rate[d] 脳 eligible_gmv_coverage[d]
daily_px[d] = monthly_px_budget 脳 raw_px[d] / sum(raw_px)
```

If PX is storewide, use the applicable full-platform GMV as the eligible base and keep rate variants such as `4.5%` and `6.5%` as separate planning cases.

## Validator JSON

```json
{
  "store": {
    "shopee_gmv": 452000,
    "tiktok_gmv": 581000,
    "forecast_full_month_gmv": 400093,
    "full_site_roi": 7
  },
  "categories": [
    {"name": "perfume", "target_gmv": 320000},
    {"name": "bundle", "target_gmv": 90000}
  ],
  "products": [
    {"name": "Leona", "target_gmv": 144000},
    {"name": "bundle", "target_gmv": 90000},
    {"name": "other", "target_gmv": 88000}
  ],
  "channels": [
    {"name": "px", "budget": 22600},
    {"name": "onsite_ads", "budget": 18080},
    {"name": "offsite_ads", "budget": 12656},
    {"name": "voucher", "budget": 7619},
    {"name": "affiliate", "budget": 3616}
  ],
  "priority_groups": [
    ["px"],
    ["onsite_ads"],
    ["offsite_ads"],
    ["voucher", "affiliate"]
  ],
  "daily": []
}
```

Populate complete category and product rows before validation. Omit `daily` for monthly-only validation; use `--require-daily` before final publishing.
