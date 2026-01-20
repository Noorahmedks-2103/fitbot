def generate_diet(data):
    days = int(data["days"])
    plan = {}

    for d in range(1, days + 1):
        plan[f"Day {d}"] = {
            "Breakfast": "Oats + Fruits",
            "Lunch": "Rice + Dal + Veggies",
            "Snacks": "Nuts / Fruits",
            "Dinner": "Protein + Salad"
        }
    return plan
