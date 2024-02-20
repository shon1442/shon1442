class ConstructionSoftware:
    def _init_(self):
        self.plans = {}

    def add_plan(self, plan):
        self.plans[plan] = {}

    def count_quantities(self, plan):
        quantities = {
            "cement": 1000,
            "bricks": 5000,
            "steel": 200,
            # וכן הלאה...
        }
        return quantities

    def compare_plans(self, plan1, plan2):
        comparison_result = {
            "differences": {
                "material": "cement",
                "plan1_quantity": 1000,
                "plan2_quantity": 800,
                # וכן הלאה...
            },
            "overall_result": "Plan1 is more cost-effective",
        }
        return comparison_result

    def generate_report(self, plan):
        report = {
            "plan_name": "Plan One",
            "date": "2024-02-20",
            "quantities": {
                "cement": 1000,
                "bricks": 5000,
                "steel": 200,
                # וכן הלאה...
            },
            "notes": "Quantities were checked and approved according to plan specifications.",
        }
        return report

    def automatic_operations(self, plan1, plan2):
        quantities_plan1 = self.count_quantities(plan1)
        quantities_plan2 = self.count_quantities(plan2)
        comparison_result = self.compare_plans(plan1, plan2)
        report_plan1 = self.generate_report(plan1)
        report_plan2 = self.generate_report(plan2)
        return quantities_plan1, quantities_plan2, comparison_result, report_plan1, report_plan2
