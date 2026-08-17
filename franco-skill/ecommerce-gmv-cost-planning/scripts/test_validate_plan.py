import copy
import unittest

from validate_plan import validate_plan


def valid_plan():
    return {
        "store": {
            "shopee_gmv": 452000,
            "tiktok_gmv": 581000,
            "full_site_roi": 7,
        },
        "categories": [
            {"name": "perfume", "target_gmv": 320000},
            {"name": "body_lotion", "target_gmv": 28000},
            {"name": "body_mist", "target_gmv": 12000},
            {"name": "body_wash", "target_gmv": 2000},
            {"name": "bundle", "target_gmv": 90000},
        ],
        "products": [
            {"name": "Leona", "target_gmv": 144000},
            {"name": "Edith", "target_gmv": 60800},
            {"name": "red_lotion", "target_gmv": 18000},
            {"name": "Emma", "target_gmv": 22400},
            {"name": "Allure", "target_gmv": 28800},
            {"name": "bundle", "target_gmv": 90000},
            {"name": "other", "target_gmv": 88000},
        ],
        "channels": [
            {"name": "onsite_ads", "budget": 22600},
            {"name": "offsite_ads", "budget": 18080},
            {"name": "px", "budget": 12656},
            {"name": "voucher", "budget": 7619},
            {"name": "affiliate", "budget": 3616},
        ],
        "priority_groups": [
            ["onsite_ads"],
            ["offsite_ads"],
            ["px"],
            ["voucher", "affiliate"],
        ],
    }


class ValidatePlanTests(unittest.TestCase):
    def test_accepts_closed_monthly_plan(self):
        result = validate_plan(valid_plan())

        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["summary"]["expense_budget"], "64571")

    def test_rejects_product_total_that_hides_bundle_in_other(self):
        plan = valid_plan()
        plan["products"] = [
            product for product in plan["products"] if product["name"] != "bundle"
        ]

        result = validate_plan(plan)

        self.assertFalse(result["ok"])
        self.assertTrue(any("product" in error.lower() for error in result["errors"]))

    def test_rejects_priority_labels_when_budget_order_conflicts(self):
        plan = valid_plan()
        plan["channels"][1]["budget"] = 11000
        plan["channels"][3]["budget"] = 14699

        result = validate_plan(plan)

        self.assertFalse(result["ok"])
        self.assertTrue(any("priority" in error.lower() for error in result["errors"]))

    def test_rejects_tiktok_expense(self):
        plan = valid_plan()
        plan["store"]["tiktok_expense_budget"] = 1000

        result = validate_plan(plan)

        self.assertFalse(result["ok"])
        self.assertTrue(any("tiktok" in error.lower() for error in result["errors"]))

    def test_validates_daily_channel_and_gmv_totals(self):
        plan = valid_plan()
        plan["daily"] = [
            {
                "date": "2026-08-01",
                "shopee_gmv": 200000,
                "tiktok_gmv": 281000,
                "channel_costs": {
                    "onsite_ads": 10000,
                    "offsite_ads": 8000,
                    "px": 6000,
                    "voucher": 3000,
                    "affiliate": 1600,
                },
            },
            {
                "date": "2026-08-02",
                "shopee_gmv": 252000,
                "tiktok_gmv": 300000,
                "channel_costs": {
                    "onsite_ads": 12600,
                    "offsite_ads": 10080,
                    "px": 6656,
                    "voucher": 4619,
                    "affiliate": 2016,
                },
            },
        ]

        result = validate_plan(plan)

        self.assertTrue(result["ok"], result["errors"])

        broken = copy.deepcopy(plan)
        broken["daily"][1]["channel_costs"]["offsite_ads"] -= 1
        result = validate_plan(broken)
        self.assertFalse(result["ok"])
        self.assertTrue(any("daily offsite_ads" in error for error in result["errors"]))


if __name__ == "__main__":
    unittest.main()
