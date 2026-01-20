state = {}

def get_response(msg):
    msg = msg.lower()

    if "hi" in msg or "hello" in msg:
        return {
            "type":"text",
            "data":"👋 Hi! I’m FitBot.\nWhat is your fitness goal?\n(fat loss / muscle gain / general)"
        }

    if "fat" in msg or "muscle" in msg or "general" in msg:
        state["goal"] = msg
        return {
            "type":"text",
            "data":"How many days do you want a plan for?\n(7 / 14 / 28)"
        }

    if msg in ["7","14","28"]:
        state["days"] = msg
        return {
            "type":"text",
            "data":"Diet preference?\n(veg / non-veg)"
        }

    if "veg" in msg:
        state["diet"] = msg
        return {
            "type":"text",
            "data":(
                "✅ Personalized Plan Ready\n\n"
                f"Goal: {state.get('goal')}\n"
                f"Days: {state.get('days')}\n"
                f"Diet: {state.get('diet')}\n\n"
                "You can now ask:\n"
                "• workout\n• diet\n• sleep\n• water"
            )
        }

    if "workout" in msg:
        return {
            "type":"list",
            "data":[
                "Warm-up – 5 mins",
                "Push-ups – 3×15",
                "Squats – 3×20",
                "Plank – 3×45 sec",
                "Jumping Jacks – 2 min"
            ]
        }

    if "diet" in msg:
        return {
            "type":"list",
            "data":[
                "Breakfast: Oats + fruits",
                "Lunch: Rice + dal + vegetables",
                "Snack: Nuts or fruits",
                "Dinner: Light veg curry"
            ]
        }

    if "sleep" in msg:
        return {"type":"text","data":"😴 Sleep 7–9 hours daily for recovery."}

    if "water" in msg:
        return {"type":"text","data":"💧 Drink 2.5–3 liters of water daily."}

    return {
        "type":"text",
        "data":"Ask me about diet, workouts, sleep, water or scan food 🍎"
    }
