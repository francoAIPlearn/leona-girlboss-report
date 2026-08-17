#!/usr/bin/env python3
import argparse
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


CENT = Decimal("0.01")


def decimal(value, field):
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric") from exc


def money(value):
    return value.quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def is_close(left, right, tolerance=CENT):
    return abs(left - right) <= tolerance


def sum_target(rows, field, errors):
    total = Decimal("0")
    for index, row in enumerate(rows):
        try:
            total += decimal(row.get(field), f"row {index + 1}.{field}")
        except ValueError as exc:
            errors.append(str(exc))
    return total


def validate_plan(plan, require_daily=False):
    errors = []
    warnings = []
    store = plan.get("store") or {}

    try:
        shopee_gmv = decimal(store.get("shopee_gmv"), "store.shopee_gmv")
        tiktok_gmv = decimal(store.get("tiktok_gmv", 0), "store.tiktok_gmv")
        full_site_roi = decimal(store.get("full_site_roi"), "store.full_site_roi")
        if shopee_gmv <= 0:
            errors.append("store.shopee_gmv must be greater than zero")
        if full_site_roi <= 0:
            errors.append("store.full_site_roi must be greater than zero")
    except ValueError as exc:
        errors.append(str(exc))
        shopee_gmv = Decimal("0")
        tiktok_gmv = Decimal("0")
        full_site_roi = Decimal("1")

    for key, value in store.items():
        normalized = key.lower()
        if "tiktok" in normalized and any(
            token in normalized for token in ("expense", "cost", "budget", "fee")
        ):
            try:
                if decimal(value, f"store.{key}") != 0:
                    errors.append("TikTok expense must be zero or omitted")
            except ValueError as exc:
                errors.append(str(exc))

    expected_budget = money(shopee_gmv / full_site_roi)

    categories = plan.get("categories") or []
    category_total = sum_target(categories, "target_gmv", errors)
    if not is_close(category_total, shopee_gmv):
        errors.append(
            f"category target total {category_total} must equal Shopee GMV {shopee_gmv}"
        )

    products = plan.get("products") or []
    product_total = sum_target(products, "target_gmv", errors)
    if not is_close(product_total, shopee_gmv):
        errors.append(
            f"product target total {product_total} must equal Shopee GMV {shopee_gmv}"
        )

    channel_rows = plan.get("channels") or []
    channel_budgets = {}
    for index, row in enumerate(channel_rows):
        name = str(row.get("name", "")).strip()
        if not name:
            errors.append(f"channel row {index + 1} requires name")
            continue
        if name in channel_budgets:
            errors.append(f"duplicate channel name: {name}")
            continue
        try:
            channel_budgets[name] = decimal(
                row.get("budget"), f"channel {name}.budget"
            )
        except ValueError as exc:
            errors.append(str(exc))

    channel_total = sum(channel_budgets.values(), Decimal("0"))
    if not is_close(channel_total, expected_budget):
        errors.append(
            f"channel budget total {channel_total} must equal ROI budget {expected_budget}"
        )

    priority_groups = plan.get("priority_groups") or []
    group_totals = []
    for group_index, group in enumerate(priority_groups):
        missing = [name for name in group if name not in channel_budgets]
        if missing:
            errors.append(
                f"priority group {group_index + 1} has unknown channels: {', '.join(missing)}"
            )
        group_totals.append(
            sum((channel_budgets.get(name, Decimal("0")) for name in group), Decimal("0"))
        )
    for index in range(len(group_totals) - 1):
        if group_totals[index] <= group_totals[index + 1]:
            errors.append(
                "priority budget order conflict: "
                f"group {index + 1}={group_totals[index]} must exceed "
                f"group {index + 2}={group_totals[index + 1]}"
            )

    daily = plan.get("daily")
    if require_daily and not daily:
        errors.append("daily plan is required")
    elif daily:
        dates = [str(row.get("date", "")) for row in daily]
        if len(dates) != len(set(dates)):
            errors.append("daily plan contains duplicate dates")
        daily_shopee = sum_target(daily, "shopee_gmv", errors)
        daily_tiktok = sum_target(daily, "tiktok_gmv", errors)
        if not is_close(daily_shopee, shopee_gmv):
            errors.append(
                f"daily Shopee GMV {daily_shopee} must equal monthly target {shopee_gmv}"
            )
        if not is_close(daily_tiktok, tiktok_gmv):
            errors.append(
                f"daily TikTok GMV {daily_tiktok} must equal monthly target {tiktok_gmv}"
            )

        daily_channel_totals = {name: Decimal("0") for name in channel_budgets}
        for row_index, row in enumerate(daily):
            costs = row.get("channel_costs") or {}
            unknown = set(costs) - set(channel_budgets)
            if unknown:
                errors.append(
                    f"daily row {row_index + 1} has unknown channels: {', '.join(sorted(unknown))}"
                )
            for name in daily_channel_totals:
                try:
                    daily_channel_totals[name] += decimal(
                        costs.get(name, 0), f"daily row {row_index + 1}.{name}"
                    )
                except ValueError as exc:
                    errors.append(str(exc))
        for name, total in daily_channel_totals.items():
            if not is_close(total, channel_budgets[name]):
                errors.append(
                    f"daily {name} total {total} must equal channel budget {channel_budgets[name]}"
                )
    else:
        warnings.append("daily plan not supplied; monthly closure only")

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "summary": {
            "shopee_gmv": str(shopee_gmv),
            "tiktok_gmv": str(tiktok_gmv),
            "expense_budget": str(expected_budget),
            "category_total": str(category_total),
            "product_total": str(product_total),
            "channel_total": str(channel_total),
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Validate ecommerce monthly GMV and channel-cost plan closure."
    )
    parser.add_argument("plan", type=Path, help="UTF-8 JSON plan file")
    parser.add_argument(
        "--require-daily", action="store_true", help="Fail when daily rows are absent"
    )
    args = parser.parse_args()

    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    result = validate_plan(plan, require_daily=args.require_daily)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["ok"] else 1)


if __name__ == "__main__":
    main()
