# 月度 GMV 与全渠道费用规划模板

这是月度 GMV 与全渠道费用规划的 4 个基础模块固定复刻模板。模板来源为腾讯表格 `8月目标案例`（`sheet_id = 31duc0`）。先按本文件生成 4 个基础模块，再按需追加新客分析等可选模块。

## 整体布局

除非用户明确要求拆分，否则整份计划放在同一个 worksheet。

顶部固定两行：

```text
Row 1: <Brand/Store> <Country> <YYYY年M月>目标与全渠道费用规划
Row 2: 口径：数据截止<date>；<current period>与<baseline period>均按同周期。Shopee SP <month>GMV目标<amount>、全站ROI <roi>、费用上限<amount>；TikTok <month>目标<status>，<included/excluded>纳入Shopee ROI。
```

结构规则：

- Every module title row is merged across the visible table width.
- Every scope, logic, note, reconciliation, or execution row is merged across its table width.
- Every table has a separate field-header row immediately below the title or logic row.
- Data rows are never merged.
- Actual-value columns stay blank until actual data exists; do not copy plan values into actual columns.
- Missing historical data stays blank and is labeled in the note/status text; do not fill with zero or use units as a GMV proxy.

样式规则：

- Total title row: dark blue fill, white bold text, 16 pt, left aligned.
- Scope/note rows: light gray fill, gray text, italic or wrapped text.
- Module title rows: blue-family fill, bold text.
- Field-header rows: visually distinct from module title rows.
- Amounts use thousands separators with no forced decimals unless the source requires decimals.
- Percent fields use percentage format; ROI uses numeric format such as `7.00`.
- Long notes and action text use wrap text.

## 模块 1：店铺目标规划

模块标题：

```text
1. 店铺目标规划
```

表头：

```text
平台 | 6月MTD（1-28） | 7月MTD（1-28） | 7月环比 | 7月预计全月 | 预计增速 vs 6月 | 8月GMV目标 | 8月目标增速 | ROI目标 | 8月费用预算 | 口径与状态
```

固定行：

```text
Shopee SP | <baseline_mtd_gmv> | <current_mtd_gmv> | <current_mtd / baseline_mtd - 1> | <current_full_month_forecast> | <current_full_month_forecast / baseline_full_month_or_mtd - 1> | <approved_sp_target_gmv> | <approved_sp_target_gmv / current_full_month_forecast - 1> | <full_site_roi> | <round(approved_sp_target_gmv / full_site_roi)> | <source and status>
TikTok TT | <baseline_mtd_gmv> | <current_mtd_gmv> | <current_mtd / baseline_mtd - 1> | <current_full_month_forecast> | <current_full_month_forecast / baseline_full_month_or_mtd - 1> | <approved_or_blank_tt_target_gmv> | <target_growth_or_blank> | <blank unless TT cost is included> | <blank unless TT cost is included> | <target and cost approval status>
<Country>合计 | <baseline total> | <current total> | <current total / baseline total - 1> | <forecast total> | <forecast total / baseline total - 1> | <blank until all platform targets approved> | <blank> | <blank> | <blank> | <why totals are blank or closed>
对账说明：<说明数据来源边界；例如 DMS、财务GMV、Confirmed GMV 与规划GMV属于不同口径，只能在同口径内比较。>
```

校验规则：

```text
SP expense budget = ROUND(SP GMV target / full-site ROI)
TikTok cost, ROI, and expense cells remain blank when TikTok is excluded from Shopee ROI.
Country total target remains blank when any platform target is pending.
```

### 模块 1.1：月度每日目标节奏

子模块标题：

```text
1.1 8月每日目标节奏
```

表头：

```text
日期 | 星期 | 活动节奏 | SP GMV目标 | SP日权重 | SP累计目标 | TT三月参考因子 | TT参考权重 | TT每日目标 | 全渠道每日目标 | SP实际 | TT实际 | SP达成率 | TT达成率 | 备注
```

固定行：

```text
<YYYY/M/1> | <weekday> | <activity node> | <daily_sp_target> | <daily_sp_target / monthly_sp_target> | <cumulative_sp_target> | <tt_reference_factor> | <normalized_tt_weight> | <blank until TT target approved> | <blank until all platform daily targets exist> | <blank> | <blank> | <blank> | <blank> | <status note>
...
<YYYY/M/last day> | <weekday> | <activity node> | <daily_sp_target> | <daily_sp_target / monthly_sp_target> | <monthly_sp_target> | <tt_reference_factor> | <normalized_tt_weight> | <blank or tt_daily_target> | <blank or total_daily_target> | <blank> | <blank> | <blank> | <blank> | <status note>
<month>合计 |  |  | <monthly_sp_target> | 100.0% | <monthly_sp_target> | <factor source label> | 100.0% | <blank or monthly_tt_target> | <blank or store_total_target> |  |  |  |  |
执行口径：<describe SP daily target source, TT weighting method, campaign/payday alignment, and why TT amount is blank when target is pending.>
```

校验规则：

```text
SUM(SP GMV目标 daily rows) = monthly SP target
SUM(SP日权重) = 100.0%
Final SP累计目标 = monthly SP target
SUM(TT参考权重) = 100.0%
```

## 模块 2：品类目标拆解

模块标题：

```text
2. 品类目标拆解（Shopee SP）
```

表头：

```text
品类 | SP订单 | SP SOB | 7月环比6月 | 8月目标GMV | 规划增幅 | 增量点
```

固定行：

```text
汇总 | <sp_orders_total> | <sp_sob_total_or_primary_sob> | <comparable_growth> | <monthly_sp_target> | <planning_growth> | <summary of main growth categories>
<core category 1> | <sp_orders> | <sp_sob> | <growth> | <target_gmv> | <planning_growth> | <concrete increment driver>
<core category 2> | <sp_orders> | <sp_sob> | <growth> | <target_gmv> | <planning_growth> | <concrete increment driver>
...
套组 | <blank if source unavailable> | <blank if source unavailable> | <growth_or_blank> | <target_gmv> | <planning_growth> | <bundle/AOV role>
口径：SP订单/SOB/环比来自<source>; <month>品类目标为规划口径，合计必须等于<monthly_sp_target>。
```

校验规则：

```text
SUM(category 8月目标GMV rows excluding 汇总) = Shopee SP target
Bundle has a dedicated row when it has a target, mechanism, price architecture, or campaign role.
Unavailable history remains blank.
```

## 模块 3：产品目标

模块标题：

```text
3. 产品目标（Confirmed GMV口径）
```

表头：

```text
产品 | 品类 | 7月GMV | 6月GMV | GMV环比 | 确认订单 | 曝光 | 点击 | CTR | 访客 | 加购访客 | 确认CVR | 8月目标GMV | 目标占比 | 产品角色 | 8月动作
```

固定行序：

```text
核心放量
拉新试用
核心稳盘
增长款
承接款
试用装
套组
Other or unmapped rows, when needed
产品目标合计
口径说明
```

数据行：

```text
<product name> | <category> | <current_period_confirmed_gmv> | <baseline_period_confirmed_gmv> | <current / baseline - 1> | <confirmed_orders> | <impressions> | <clicks> | <clicks / impressions> | <visitors> | <add_to_cart_visitors> | <confirmed_orders / clicks or defined confirmed CVR> | <target_gmv> | <target_gmv / monthly_sp_target> | <product role> | <specific month action>
```

合计和说明行：

```text
产品目标合计 |  | <sum current GMV> | <sum baseline GMV> | <current total / baseline total - 1> | <sum confirmed orders> | <sum impressions> | <sum clicks> | <sum clicks / sum impressions> | <sum visitors> | <sum add-to-cart visitors> | <sum confirmed orders / sum clicks or defined confirmed CVR> | <monthly_sp_target> | 100.0% | 闭合校验 | 产品目标合计应等于品类目标与店铺SP目标
口径：<本期/上期窗口和来源>；Confirmed Order GMV 是产品目标基准口径。无法映射的产品保持空白，不用销量、代理指标或 0 替代。
```

校验规则：

```text
SUM(product 8月目标GMV excluding total row) = Shopee SP target
SUM(product 目标占比 excluding total row) = 100.0%
Product rows with unavailable historical metrics keep history blank and label the reason in action or note.
```

## 模块 4：渠道费用规划与每日节奏

模块标题：

```text
4. 渠道费用规划
```

逻辑行：

```text
逻辑：总费用=<monthly_sp_target>÷<full_site_roi>=<expense_budget>；优先级为PX项目 > 站内广告 > 站外广告 > 优惠券/联盟。
```

汇总表头：

```text
层级 | 费用项目 | 预算基数 | 8月目标费比 | 8月预算 | 资源优先级 | 控制口径
```

固定行：

```text
全站 | 全站费用 | <monthly_sp_target> | <expense_budget / monthly_sp_target> | <expense_budget> | — | Shopee GMV÷全部费用=<full_site_roi>
站内 | 站内费用合计 | <monthly_sp_target> | <onsite_total_budget / monthly_sp_target> | <onsite_total_budget> | — | PX+站内广告+优惠券+联盟
站内 | PX项目 | <eligible_or_monthly_sp_target> | <px_budget / monthly_sp_target> | <px_budget> | 1-最高 | <PX control rule>
站内 | 站内广告 | <monthly_sp_target> | <onsite_ads_budget / monthly_sp_target> | <onsite_ads_budget> | 2 | 按独立日权重分配，广告ROAS单独监控
站外 | 站外广告 | <monthly_sp_target> | <offsite_ads_budget / monthly_sp_target> | <offsite_ads_budget> | 3 | 只做增量验证，低效渠道及时收缩
站内 | 优惠券 | <monthly_sp_target> | <voucher_budget / monthly_sp_target> | <voucher_budget> | 4-其他 | 按GMV与活动费率归一
站内 | 联盟 | <monthly_sp_target> | <affiliate_budget / monthly_sp_target> | <affiliate_budget> | 4-其他 | 按GMV与活动费率归一
效率 | <month>全站ROI | <monthly_sp_target> | <full_site_roi> | <expense_budget> | 审批值 | 预算超额必须同步上调GMV或重新审批
模块4预算合计为<expense_budget>；实际录入列在产生数据前保持空白，不把计划值当实际值。
```

校验规则：

```text
全站费用 budget = ROUND(monthly SP target / full-site ROI)
PX + 站内广告 + 站外广告 + 优惠券 + 联盟 = 全站费用 budget
Priority group budget order follows the approved priority.
```

### 模块 4.1：渠道每日费用节奏

子模块标题：

```text
4.1 渠道每日费用节奏
```

表头：

```text
日期 | 星期 | 活动节奏 | SP GMV目标 | PX预算 | 站内广告 | 站外广告 | 优惠券 | 联盟 | 计划总费用 | 当日费比 | 实际SP GMV | 实际PX | 实际站内广告 | 实际站外 | 实际其他 | 实际全站ROI
```

每日行：

```text
<YYYY/M/D> | <weekday> | <activity node> | <daily_sp_target> | <daily_px_budget> | <daily_onsite_ads_budget> | <daily_offsite_ads_budget> | <daily_voucher_budget> | <daily_affiliate_budget> | <sum daily channel budgets> | <daily planned cost / daily SP target> | <blank> | <blank> | <blank> | <blank> | <blank> | <blank>
```

合计和说明行：

```text
<month>合计 |  |  | <monthly_sp_target> | <monthly_px_budget> | <monthly_onsite_ads_budget> | <monthly_offsite_ads_budget> | <monthly_voucher_budget> | <monthly_affiliate_budget> | <expense_budget> | <expense_budget / monthly_sp_target> |  |  |  |  |  |
4.1执行口径：五个渠道分别按月预算归一后拆日，合计精确闭合；实际字段保持空白。
```

校验规则：

```text
SUM(daily SP GMV目标) = monthly SP target
SUM(daily PX预算) = monthly PX budget
SUM(daily 站内广告) = monthly onsite ads budget
SUM(daily 站外广告) = monthly offsite ads budget
SUM(daily 优惠券) = monthly voucher budget
SUM(daily 联盟) = monthly affiliate budget
SUM(daily 计划总费用) = expense budget
```

## 可选模块 5：品牌新老客情况

当 Brand Portal Buyer 数据纳入计划表时，模块 5 必须按腾讯表格 `8月目标案例` 的结构追加在模块 4.1 后面。不要使用简化表头替代该结构。

模块标题：

```text
5. 品牌新老客情况（<Brand> <Country>）
```

对比口径行：

```text
对比口径：<本期日期范围> vs <上期日期范围>；来源为<account/profile> Brand Portal Consumer Insights -> Buyer，店铺<shop_id>。
```

### 模块 5.1：店铺维度新老客同周期对比

子模块标题：

```text
5.1 店铺维度新老客同周期对比
```

表头：

```text
周期 | 本期总买家 | 上期总买家 | 总买家环比 | 本期新买家 | 上期新买家 | 新买家环比 | 本期老买家 | 上期老买家 | 老买家环比 | 本期新客占比 | 上期新客占比 | 占比变化 | 结论
```

固定行：

```text
<本期MTD> | <current_all_buyers> | <baseline_all_buyers> | <current_all / baseline_all - 1> | <current_new_buyers> | <baseline_new_buyers> | <current_new / baseline_new - 1> | <current_existing_buyers> | <baseline_existing_buyers> | <current_existing / baseline_existing - 1> | <current_new / current_all> | <baseline_new / baseline_all> | <current_new_share - baseline_new_share> | MTD同周期
<week 1> | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | <short conclusion>
<week 2> | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | <short conclusion>
<week 3> | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | <short conclusion>
<week 4> | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | <short conclusion>
结论：<one merged row summarizing whether total buyers, new buyers, and existing buyers improved; call out weak weeks explicitly.>
```

校验规则：

```text
本期总买家 = 本期新买家 + 本期老买家
上期总买家 = 上期新买家 + 上期老买家
All comparison rows use same-day-count windows.
```

### 模块 5.2：产品维度新老客同周期对比

子模块标题：

```text
5.2 产品维度新老客同周期对比（Top20；仅完整同天数观测显示严格环比）
```

表头：

```text
产品 | Item ID | 本期新客观测累计 | 上期新客观测累计 | 新客环比（严格） | 本期老客观测累计 | 上期老客观测累计 | 老客环比（严格） | 本期新客占比 | 上期新客占比 | 占比变化（严格） | 新客占比条 | Top20观测覆盖 A/N/E | 动作
```

数据行：

```text
<product name> | <item_id> | <current_new_observed_sum> | <baseline_new_observed_sum> | <strict_new_growth_or_blank> | <current_existing_observed_sum> | <baseline_existing_observed_sum> | <strict_existing_growth_or_blank> | <current_new_share> | <baseline_new_share> | <strict_share_change_or_blank> | <bar> | 本期 <A/N/E>；上期 <A/N/E> | <short action>
```

口径说明行：

```text
口径说明：产品数据为每日各 Buyer Segment Top20 出现次数累计，不是唯一MTD买家；未进入某日Top20记为 not_observed，不补0。仅两期均完整观测同天数时显示严格环比；空白表示不等期。新客占比只用同日同时进入 All/New Top20 的对齐日期。
```

校验规则：

```text
Top20观测覆盖 A/N/E must be present for every product row.
Strict MoM fields remain blank unless both periods have equal and complete observation windows.
Top20 unobserved days are not zero-filled.
```

### 模块 5.3：店铺月度明细

子模块标题：

```text
5.3 店铺月度明细
```

表头：

```text
周期 | 总买家逐日累计 | 新买家逐日累计 | 老买家逐日累计 | 新客占比 | 观测天数 | 状态 | 口径
```

固定行：

```text
<baseline period> | <baseline_all_daily_sum> | <baseline_new_daily_sum> | <baseline_existing_daily_sum> | <baseline_new_share> | <observed_days> | <完整/缺失> | 逐日Buyer occurrences累计
<current period> | <current_all_daily_sum> | <current_new_daily_sum> | <current_existing_daily_sum> | <current_new_share> | <observed_days> | <完整/缺失> | 逐日Buyer occurrences累计
```

### 模块 5.4：数据来源与完整性

子模块标题：

```text
5.4 数据来源与完整性
```

固定说明行：

```text
来源：Shopee Brand Portal Consumer Insights -> Buyer；账号<account>；页面品牌显示<brand>；Region=<region>；Shop=<shop_id>。
完整性：<date_count>个自然日全部成功；Summary与All/New/Existing Top20共<response_count>个日级响应；缺失端点=<count>。
店铺口径：Summary直接返回 All Buyers 与 New Buyers，Existing Buyers = All - New；累计为每日Buyer occurrences相加，不代表去重月度买家。
产品口径：产品数据为每日各 Buyer Segment Top20 出现次数累计，不是唯一MTD买家；未进入某日Top20记为 not_observed，不补0。
Buyer侧信号：<短句总结强/弱链接>。预算动作需再联查GMV、CVR、ROAS与库存后执行。
```

## 最终读回

声明完成前，必须读回在线表格或生成文件，并确认：

```text
总标题和总口径说明行存在。
模块 1、1.1、2、3、4、4.1 标题存在。
每个模块/子模块都有本模板规定的精确表头。
合并行仅限标题、说明、逻辑、对账和执行口径行。
数据行没有合并单元格。
店铺、品类、产品、渠道和每日合计全部闭合。
实际字段在真实数据产生前保持空白。
如包含模块 5，5.1、5.2、5.3、5.4 的标题、表头、口径说明、Top20 A/N/E 覆盖和数据完整性说明存在。
没有公式错误、隐藏旧口径文本，或由旧合并单元格导致的可见空表头。
```
