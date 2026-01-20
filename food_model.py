
def analyze_food_image(filepath):
    # Placeholder: you can replace with real model later
    return {
        "food": "Unknown food (demo)",
        "calories": 250,
        "nutrition": {
            "protein": "10 g",
            "carbs": "30 g",
            "fat": "8 g"
        }
    }

def predict_food_calories(food_name):
    db = {
        "rice": 130,
        "chapati": 80,
        "apple": 52,
        "banana": 89,
        "egg": 78,
        "chicken": 200
    }
    key = food_name.lower().strip()
    if key in db:
        return f"{key.title()} has about {db[key]} kcal per 100 g (approx)."
    return "I don't have calorie data for that food yet."
