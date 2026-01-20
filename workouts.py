def generate_workout(goal, days):
    base = {
        "muscle": ["Pushups", "Pullups", "Squats", "Bench Press", "Deadlift"],
        "fat": ["Jumping Jacks", "Burpees", "Mountain Climbers"],
        "strength": ["Deadlift", "Squats", "Overhead Press"]
    }

    plan = {}
    for d in range(1, days + 1):
        plan[f"Day {d}"] = base.get(goal.lower(), base["muscle"])
    return plan
