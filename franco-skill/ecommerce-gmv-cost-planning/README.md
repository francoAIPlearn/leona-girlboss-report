# ecommerce-gmv-cost-planning

可复用的电商 GMV 与全渠道费用规划 Skill，适用于 Shopee、TikTok 等平台的月度目标、品类/产品拆分、渠道预算和每日节奏校验。

## 入口

- `SKILL.md`：Skill 主入口与完整工作流
- `agents/openai.yaml`：Codex Skill 元数据
- `references/monthly-plan-template.md`：四大基础模块及可选新客模块模板
- `references/planning-schema.md`：字段定义、闭环公式和 JSON 校验契约
- `scripts/validate_plan.py`：计划 JSON 校验器
- `references/example-plan.json`：脱敏示例输入

## 离线验证

```powershell
python -m py_compile scripts/validate_plan.py scripts/test_validate_plan.py
python scripts/test_validate_plan.py
python scripts/validate_plan.py references/example-plan.json
```

示例只包含规划数字，不含账号、凭证、Cookie、Token、Webhook 或签名 URL。生产使用时请先锁定国家、店铺、月份、平台口径、ROI 分母和数据来源，再按模板生成计划并读回最终表格。
