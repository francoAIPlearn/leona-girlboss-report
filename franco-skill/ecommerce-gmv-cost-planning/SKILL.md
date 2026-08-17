---
name: ecommerce-gmv-cost-planning
description: Use when planning or revising monthly ecommerce GMV targets, category and product allocations, full-site ROI or expense ratios, channel budgets, daily pacing, bundle splits, or target-planning spreadsheets for Shopee, TikTok, and similar marketplaces.
---

# Ecommerce GMV and Cost Planning

## Purpose

Build a closed monthly plan from store GMV down to category, product, channel cost, and daily execution. Preserve source truth, keep bundles explicit, separate channel metrics, and prove every subtotal before publishing.

## Required inputs

Collect or confirm:

- Country, store, planning month, currency, and timezone.
- Historical baseline and whether it is MTD, same-period, forecast, or full month.
- Whether a partial month must be projected to a full month before target-growth comparison.
- GMV target by platform. Keep Shopee and TikTok separate.
- Full-site ROI or expense-ratio constraint and its denominator.
- Category targets, product priorities, bundle strategy, and channel priority.
- Activity calendar, payday, campaign dates, inventory constraints, and available actuals.
- Target artifact: Tencent Sheet, Google Sheet, Excel, CSV, or written plan.

Do not invent scoring weights, growth targets, ROI assumptions, or missing historical values. Mark user-provided targets as planning inputs; calculate arithmetic growth separately.

## Workflow

### 1. Lock the planning scope

Write a one-line scope contract before calculating:

```text
Country + store + month + platform GMV targets + expense denominator + channels included/excluded
```

If TikTok has a GMV target but no budget, exclude TikTok GMV and expenses from Shopee ROI. Never use combined store GMV as the Shopee ROI numerator.

Read `references/planning-schema.md` when formulas, field definitions, or JSON validation input are needed. Read `references/monthly-plan-template.md` before building or editing the visible four-module execution sheet.

### 2. Build the store target

Show historical baseline, current forecast, target GMV, target growth, target ROI, expense ceiling, and expense ratio.

If the baseline month is incomplete, first compute a full-month forecast from current actuals. Use that forecast to explain target growth; do not compare a raw MTD number against a full-month target.

Classify every target field as one of: `approved_target`, `calculated_forecast`, `planning_assumption`, or `pending_confirmation`. A pending target stays blank, is labeled as pending, and must not enter totals or growth calculations. Do not turn a historical forecast into an approved target merely to complete a table.

Use:

```text
expense_budget = ROUND(channel_gmv / full_site_roi)
full_site_expense_ratio = expense_budget / channel_gmv
```

Distinguish full-site ROI from advertising ROAS. Do not derive the full channel budget from advertising ROAS.

### 3. Split categories

Allocate only the platform target being planned. Require:

```text
sum(category_target_gmv) = platform_target_gmv
```

Keep bundles as a separate category when they have a dedicated target, mechanism, price architecture, or campaign role. Do not hide bundles inside `other`.

Keep planning growth labels separate from calculated growth. If the source provides a target growth field that is not arithmetically reproducible, label it `planning_growth` rather than silently recalculating it.

### 4. Split products

List core products, growth products, bundles, and residual products. Calculate residual only after explicit rows:

```text
other_target = platform_target - sum(explicit_product_targets)
```

Require product targets to close to the same platform target. Leave historical GMV blank when no reliable product-level baseline exists; do not replace missing history with zero.

### 5. Split channel expenses

Use the hierarchy:

```text
full-site expense
  onsite expense
    onsite ads
    affiliate
    voucher
    PX / platform program
  offsite expense
```

Convert the stated priority into budget order, not labels only. Treat `PX > onsite ads > offsite > other` as a default soft ordering template, not a fixed rule. Confirm the actual priority order with the responsible owner first, then use the agreed order in the sheet and in validation. Compare `other` as the sum of all channels in that group.

For Malaysia / MY marketplace planning, default PX and PX+ to not applicable: do not create PX or PX+ project rows, budgets, daily pacing, or ROI deductions unless the user provides explicit market evidence or an approved project target. If copying a reference sheet that contains PX or PX+, remove those rows or mark them `not_applicable_MY`; do not silently carry them into the Malaysia plan.

Require:

```text
sum(channel_budgets) = expense_budget
priority_group_1_budget > priority_group_2_budget > ...
```

If exact channel ratios are not provided, present the proposed split as an assumption and keep the total ROI constraint unchanged.
If PX is storewide, calculate it from the applicable full-platform GMV and the stated rate version. Do not invent a coverage ratio to force the budget to close.

### 6. Build independent daily rhythms

Keep Shopee and TikTok GMV rhythms separate. Normalize every monthly series so its daily rows sum exactly to the monthly target.

- Onsite ads and offsite ads: allocate by independent day weights.
- Affiliate and voucher: start from daily GMV-linked rates, then normalize to the monthly budget.
- PX: calculate `commission rate × eligible GMV`. Never invent an eligible-GMV coverage rate to force PX into the expense ceiling.
- Default PX eligible GMV to 100% of the applicable platform GMV when the program applies storewide. Reduce coverage only when an authoritative program rule, exported field, or user-provided eligible-SKU GMV supports it.
- If PX only has rate variants such as `4.5%` and `6.5%`, keep them as supported planning cases instead of averaging them into a fake monthly rate.
- If PX eligibility is unknown, show the 100%-coverage result as the planning case and surface the resulting ROI or budget conflict before publishing.
- Apply campaign, weekend, payday, preheat, and post-campaign patterns only when supported by source data or explicit assumptions.
- Put rounding residuals on the largest-weight day or final day; never leave a broken monthly total.

### 7. Add new-customer analysis

When the plan includes Brand Portal Buyer data, add a fifth visible section after channel expenses:

```text
模块 5｜新客分析
```

Use Brand Portal `Consumer Insights -> Buyer` only. Do not use GMV, orders, or units sold as a proxy for new buyers. Keep this section outside GMV and expense closure formulas.

Split the section into:

1. 5.1｜店铺维度新老客同周期对比
2. 5.2｜产品维度新老客同周期对比
3. 5.3｜店铺月度明细
4. 5.4｜数据来源与完整性

Use the same layout as the Tencent Sheet reference `8月目标案例`: module title row, comparison-scope row, submodule title rows, independent header rows, data rows, conclusion/source rows. For the store comparison block, use:

```text
周期 | 本期总买家 | 上期总买家 | 总买家环比 | 本期新买家 | 上期新买家 | 新买家环比 | 本期老买家 | 上期老买家 | 老买家环比 | 本期新客占比 | 上期新客占比 | 占比变化 | 结论
```

For the product comparison block, use:

```text
产品 | Item ID | 本期新客观测累计 | 上期新客观测累计 | 新客环比（严格） | 本期老客观测累计 | 上期老客观测累计 | 老客环比（严格） | 本期新客占比 | 上期新客占比 | 占比变化（严格） | 新客占比条 | Top20观测覆盖 A/N/E | 动作
```

For the store monthly detail block, use:

```text
周期 | 总买家逐日累计 | 新买家逐日累计 | 老买家逐日累计 | 新客占比 | 观测天数 | 状态 | 口径
```

The data-source block has no table header; use merged note rows for source, completeness, store mouth, product Top20 observation mouth, and buyer-side signal summary.

Required formulas:

```text
总买家环比 = 本期总买家 / 上期总买家 - 1
新买家环比 = 本期新买家 / 上期新买家 - 1
老买家环比 = 本期老买家 / 上期老买家 - 1
本期新客占比 = 本期新买家 / 本期总买家
上期新客占比 = 上期新买家 / 上期总买家
占比变化 = 本期新客占比 - 上期新客占比
店铺校验 = 总买家 - 新买家 - 老买家
```

Status and role rules:
- Store rows should include the MTD same-period row and weekly slices when available, then a merged conclusion row.
- Product rows cover only the visible Top20 observed products. Use the coverage column in the exact form `本期 A/N/E；上期 A/N/E`, where A/N/E means All/New/Existing observed-day counts.
- Show strict product MoM only when both periods have equal and complete observation windows; otherwise leave strict comparison fields blank.
- Missing, unauthorized, unobserved, or Top20-outside data stays blank and is labeled in coverage/source notes; never fill with zero.
- If `店铺校验` is not zero, preserve source values, state the mismatch in 5.4, and do not make a business judgment from the affected row.

Actions and conclusions must stay short, operational, and risk-aware. Product actions should read like the reference: `8.8与发薪日重点放量，监控库存与确认CVR`, `承接低门槛拉新并向主链接转化`, `保预算，强化老客复购与套购`, `先验证高增速可持续性，再逐步加量`, or `历史链接无法准确映射，保持空白并补采`.

### 8. Publish the execution sheet

Build the visible execution sheet from `references/monthly-plan-template.md`; do not improvise from the shorter recommended-column summary. The four base sections are fixed:

1. Store target planning
2. Category target breakdown
3. Product targets
4. Channel expense plan and daily rhythm

When Brand Portal Buyer data is included, append the optional fifth section after the four base sections:

```text
5. 新客分析
```

Show actual-input columns beside plan columns. Use consistent currency and percentage formats. Keep TikTok expense fields absent when TikTok budget is excluded.

Every table block must have a visible section title row, a separate field-header row, and data rows. Do not treat a blue merged section title such as `Store target planning` or `Product targets` as the field header. When rebuilding or inserting rows, write the field-header row explicitly before writing data.

For Tencent Sheet or Excel layout rules, read `references/spreadsheet-output.md`. When editing Tencent documents, **REQUIRED SUB-SKILL:** use `tencent-docs`. For standalone spreadsheet files, use `spreadsheets`.

### 9. Validate before claiming completion

Create a JSON snapshot matching `references/planning-schema.md`, then run:

```powershell
python scripts/validate_plan.py path\to\plan.json
python scripts/validate_plan.py path\to\plan.json --require-daily
```

Do not publish until all of these hold:

- Store, category, product, and daily GMV totals close.
- Channel budgets equal the ROI-derived expense ceiling.
- Priority groups descend by actual budget.
- Daily channel totals equal monthly channel budgets.
- TikTok expenses are zero or absent when excluded.
- The four base sections match `references/monthly-plan-template.md`, including titles, submodule titles, header rows, total rows, and scope/execution notes.
- Each visible table block has a nonblank field-header row immediately below its section title or grouped title.
- New-customer rows, when included, match the `8月目标案例` module 5 layout: 5.1 store same-period comparison, 5.2 product Top20 observed comparison, 5.3 store monthly detail, and 5.4 source/completeness notes.
- No formula errors, stale old-scope text, hidden merged rows, or partial data.

After writing an online sheet, read back the key totals and formulas from the live document. Local calculations alone are not proof of completion.

For source-constrained product planning, retain an auditable source label and date window for each historical metric. Leave an unavailable product metric blank and label it `unobserved`; never substitute sales units, a proxy metric, or zero for historical GMV. Perform one independent read-only review of the delivered sheet when the output is used for operational budgeting.

## Common failures

- Using combined Shopee + TikTok GMV to calculate Shopee ROI.
- Treating full-site ROI and ad ROAS as the same metric.
- Copying a reference workbook's structure and also copying its ratios without approval.
- Listing a priority order that contradicts budget amounts.
- Comparing a partial-month MTD baseline directly against a full-month target without first forecasting the month.
- Reducing PX expense with an unverified eligible-GMV coverage assumption.
- Carrying PX or PX+ rows into a Malaysia / MY plan without explicit evidence that those projects exist.
- Leaving bundles inside `other` after assigning them a distinct target.
- Filling unavailable history with zero.
- Updating totals but not daily formulas.
- Restoring data rows after an insert or clear operation but leaving the field-header row blank.
- Trusting visible blanks without checking merged cells and underlying values.
- Treating a forecast or assumption as an approved target.
- Filling an unavailable product baseline with units sold, a proxy, or zero.
