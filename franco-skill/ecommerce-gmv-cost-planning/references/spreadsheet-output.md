# Spreadsheet Output Contract

For the four base monthly-planning modules, use `references/monthly-plan-template.md` as the fixed replication template. The sections below are only a compact orientation and do not replace the template. Do not build the visible sheet from these recommended-column summaries alone.

## Section 1: Store target planning

Recommended columns:

```text
Platform | Baseline GMV | Current forecast | Attainment | Growth |
Target GMV | Target growth | Full-site ROI | All-channel expense budget
```

Show TikTok GMV but leave TikTok expense, ROI, and cost columns blank when excluded.

## Section 2: Category targets

Recommended columns:

```text
Category | Historical scale | Current mix | Comparable growth |
Target GMV | Planning growth | Increment focus
```

Add a dedicated bundle row when bundles have a target or operating mechanism.
When the baseline month is incomplete, use the forecast full-month baseline for the growth explanation and keep the raw MTD figure separate.

## Section 3: Product targets

Recommended columns:

```text
Product | Category | Historical GMV | Target GMV | Target share |
Calculated growth | Product role | Action
```

Order rows as core products, growth products, bundles, and `other`. Recalculate all target-share formulas when inserting a new row.

## Section 4: Channel expenses

Summary columns:

```text
Level | Expense item | Budget denominator | Historical ratio |
Target ratio | Target budget | Change | Control rule | Priority
```

Daily columns should expose each channel's planning driver and budget separately. Keep actual inputs beside planned amounts and calculate cumulative burn and actual full-site ROI.
Sort rows by the agreed budget priority. If the brief proposes `PX > onsite ads > offsite > other`, treat it as a starting template, confirm the final order with the responsible owner, then keep the agreed order visible in the sheet and do not bury PX in a residual row.

## Section 5: New-customer analysis

Add this section only when Brand Portal Buyer data is part of the planning artifact. Match the Tencent Sheet reference `8月目标案例` module 5 layout: module title row, comparison-scope row, 5.1 store comparison, 5.2 product Top20 observed comparison, 5.3 store monthly detail, and 5.4 source/completeness notes. Use Brand Portal `Consumer Insights -> Buyer` as the source.

Module title and comparison scope:

```text
5. 品牌新老客情况（<Brand> <Country>）
对比口径：<current period> vs <baseline period>；来源为<account/profile> Brand Portal Consumer Insights -> Buyer，店铺<shop_id>。
```

5.1 store comparison title and columns:

```text
5.1 店铺维度新老客同周期对比
周期 | 本期总买家 | 上期总买家 | 总买家环比 | 本期新买家 | 上期新买家 | 新买家环比 | 本期老买家 | 上期老买家 | 老买家环比 | 本期新客占比 | 上期新客占比 | 占比变化 | 结论
```

5.2 product comparison title and columns:

```text
5.2 产品维度新老客同周期对比（Top20；仅完整同天数观测显示严格环比）
产品 | Item ID | 本期新客观测累计 | 上期新客观测累计 | 新客环比（严格） | 本期老客观测累计 | 上期老客观测累计 | 老客环比（严格） | 本期新客占比 | 上期新客占比 | 占比变化（严格） | 新客占比条 | Top20观测覆盖 A/N/E | 动作
```

5.3 store monthly detail title and columns:

```text
5.3 店铺月度明细
周期 | 总买家逐日累计 | 新买家逐日累计 | 老买家逐日累计 | 新客占比 | 观测天数 | 状态 | 口径
```

5.4 source and completeness:

```text
5.4 数据来源与完整性
来源：Shopee Brand Portal Consumer Insights -> Buyer；账号<account>；页面品牌显示<brand>；Region=<region>；Shop=<shop_id>。
完整性：<date_count>个自然日全部成功；Summary与All/New/Existing Top20共<response_count>个日级响应；缺失端点=<count>。
店铺口径：Summary直接返回 All Buyers 与 New Buyers，Existing Buyers = All - New；累计为每日Buyer occurrences相加，不代表去重月度买家。
产品口径：产品数据为每日各 Buyer Segment Top20 出现次数累计，不是唯一MTD买家；未进入某日Top20记为 not_observed，不补0。
Buyer侧信号：<short operational summary>; 预算动作需再联查GMV、CVR、ROAS与库存后执行。
```

Calculations:

```text
总买家环比 = 本期总买家 / 上期总买家 - 1
新买家环比 = 本期新买家 / 上期新买家 - 1
老买家环比 = 本期老买家 / 上期老买家 - 1
本期新客占比 = 本期新买家 / 本期总买家
上期新客占比 = 上期新买家 / 上期总买家
占比变化 = 本期新客占比 - 上期新客占比
店铺校验 = 总买家 - 新买家 - 老买家
```

Recommendation style:

- Use short, operational sentences.
- State one action and one boundary.
- Check source or conversion before budget changes when data is incomplete.
- Examples: `保预算，放大同款素材和入口。`, `控折扣，先提转化，不盲目扩量。`, `适合复购承接，不作为拉新主推。`, `数据缺失，先补导出，不做资源倾斜。`

Rules:

- Use same-day-count comparison windows only. If unavailable, leave comparison fields blank and set status to `缺对比`.
- Leave missing, unauthorized, unobserved, and Top20-outside values blank; do not fill with zero.
- Product strict comparison fields stay blank unless both periods have equal and complete observation windows.
- If `总买家 != 新买家 + 老买家`, preserve source values and disclose the mismatch in 5.4.
- Do not merge Buyer rows into GMV or expense closure formulas.

## Formatting

- Use one currency format and one percentage format per semantic field.
- Color only editable inputs; keep formulas visually distinct.
- Keep every table as `section title row -> field-header row -> data rows -> optional note/total row`.
- Style section title rows and field-header rows differently; never let a merged title row replace the field-header row.
- Show total rows with a consistent subtotal style.
- Keep long action text wrapped; do not merge data columns to simulate width.
- Freeze only stable title/header rows and the identifying first column.

## Tencent Sheet safeguards

1. Query the target `sheet_id`; never update other worksheets by name guessing.
2. Read existing merged cells before rebuilding a range.
3. Explicitly unmerge stale ranges that intersect data rows. Clearing content does not reliably remove old merges.
4. Merge only title, section, and note rows. Never merge daily or product data rows.
5. After insertions, update formulas that point to moved total rows.
6. After inserting or deleting rows, recalculate all downstream row indexes before writing additional content.
7. Write field-header rows explicitly after any range rebuild; do not rely on copied formatting or old merged cells to preserve them.
8. Read back the live rows after styling. A value can exist underneath a stale merge while appearing blank in the UI.
9. Verify no old scope text remains, such as an obsolete statement that expenses cover only one channel.
10. Visually inspect or screenshot table boundaries when a user reports a blank header; a value-only readback may miss a merged-cell display issue.

## Final readback

Confirm from the live artifact:

```text
top title and overall scope rows
base modules 1, 1.1, 2, 3, 4, and 4.1 from monthly-plan-template.md
exact header rows, total rows, and scope/execution notes for the four base modules
platform targets
category total
product total and 100% share
channel budgets and priority order
full-site ROI and expense ratio
daily GMV and channel totals
nonblank field-header row for each table block
absence of formula errors
absence of unintended merged data rows
new-customer module 5.1, 5.2, 5.3, and 5.4 layout
new-customer source/completeness notes and Top20 observed A/N/E coverage
```
