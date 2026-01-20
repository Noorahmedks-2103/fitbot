import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="NoorFit AI",
    page_icon="💪",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("💪 NoorFit AI")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "BMI Calculator",
        "Workout Plan",
        "Diet Plan",
        "Chatbot",
        "About"
    ]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.title("Welcome to NoorFit AI 💪")
    st.subheader("Your personal fitness & health assistant")

    st.write("""
    NoorFit AI helps you:
    - Calculate BMI
    - Get workout suggestions
    - Follow simple diet plans
    - Chat with a fitness assistant
    - Stay consistent with fitness
    """)

    st.success("✅ Streamlit is working perfectly!")

# ---------------- BMI CALCULATOR ----------------
elif menu == "BMI Calculator":
    st.title("📊 BMI Calculator")

    col1, col2 = st.columns(2)

    with col1:
        weight = st.number_input("Enter your weight (kg)", min_value=1.0)

    with col2:
        height = st.number_input("Enter your height (cm)", min_value=50.0)

    if st.button("Calculate BMI"):
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        bmi = round(bmi, 2)

        # Save BMI in session (for chatbot)
        st.session_state["bmi"] = bmi

        st.write(f"### Your BMI is: **{bmi}**")

        if bmi < 18.5:
            st.warning("Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Normal weight ✅")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Obese")

# ---------------- WORKOUT PLAN ----------------
elif menu == "Workout Plan":
    st.title("🏋️ Workout Plan")

    goal = st.selectbox(
        "Select your goal",
        ["Weight Loss", "Muscle Gain", "General Fitness"]
    )

    if goal == "Weight Loss":
        st.write("""
        **Workout Plan (Weight Loss):**
        - Brisk walking / jogging – 30 min
        - Jumping jacks – 3 × 20
        - Squats – 3 × 15
        - Plank – 3 × 30 sec
        """)

    elif goal == "Muscle Gain":
        st.write("""
        **Workout Plan (Muscle Gain):**
        - Push-ups – 4 × 12
        - Pull-ups – 3 × 8
        - Squats – 4 × 15
        - Dumbbell curls – 3 × 12
        """)

    else:
        st.write("""
        **Workout Plan (General Fitness):**
        - Walking – 20 min
        - Stretching – 10 min
        - Light yoga
        """)

# ---------------- DIET PLAN ----------------
elif menu == "Diet Plan":
    st.title("🥗 Diet Plan")

    diet = st.selectbox(
        "Choose your preference",
        ["Vegetarian", "Non-Vegetarian"]
    )

    if diet == "Vegetarian":
        st.write("""
        **Vegetarian Diet Plan:**
        - Breakfast: Oats + fruits
        - Lunch: Rice + dal + vegetables
        - Snack: Nuts / fruits
        - Dinner: Chapati + paneer
        """)

    else:
        st.write("""
        **Non-Vegetarian Diet Plan:**
        - Breakfast: Eggs + fruits
        - Lunch: Rice + chicken/fish
        - Snack: Boiled eggs
        - Dinner: Chapati + chicken
        """)

# ---------------- CHATBOT ----------------
elif menu == "Chatbot":
    st.title("🤖 NoorFit AI – Fitness Chatbot")
    st.write("Ask me about BMI, workouts, diet, or fitness tips.")

    if "chat" not in st.session_state:
        st.session_state.chat = []

    # Show chat history
    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask a fitness question...")

    if user_input:
        # Save user message
        st.session_state.chat.append(
            {"role": "user", "content": user_input}
        )

        text = user_input.lower()
        reply = ""

        # ---- BMI response ----
        if "bmi" in text:
            if "bmi" in st.session_state:
                bmi = st.session_state["bmi"]
                if bmi < 18.5:
                    reply = f"Your BMI is {bmi}. You are underweight. Focus on healthy weight gain."
                elif bmi < 25:
                    reply = f"Your BMI is {bmi}. You are in the normal range. Maintain your routine."
                elif bmi < 30:
                    reply = f"Your BMI is {bmi}. You are overweight. Cardio and diet control will help."
                else:
                    reply = f"Your BMI is {bmi}. This is in the obesity range. Professional advice is recommended."
            else:
                reply = "Please calculate your BMI first using the BMI Calculator."

        # ---- Workout response ----
        elif "workout" in text or "exercise" in text:
            reply = (
                "A balanced workout includes:\n"
                "- Cardio (3–4 days/week)\n"
                "- Strength training\n"
                "- Flexibility exercises\n"
                "- Proper rest"
            )

        # ---- Diet response ----
        elif "diet" in text or "food" in text:
            reply = (
                "A healthy diet includes:\n"
                "- Protein (eggs, chicken, dal)\n"
                "- Complex carbohydrates\n"
                "- Fruits & vegetables\n"
                "- Plenty of water"
            )

        # ---- Weight loss ----
        elif "weight loss" in text:
            reply = (
                "For weight loss:\n"
                "- Maintain calorie deficit\n"
                "- Daily physical activity\n"
                "- Avoid sugar & junk food"
            )

        # ---- Default ----
        else:
            reply = (
                "I can help you with:\n"
                "- BMI explanation\n"
                "- Workout guidance\n"
                "- Diet tips\n"
                "Try asking about BMI or workouts."
            )

        # Save bot reply
        st.session_state.chat.append(
            {"role": "assistant", "content": reply}
        )

        with st.chat_message("assistant"):
            st.markdown(reply)

# ---------------- ABOUT ----------------
elif menu == "About":
    st.title("ℹ️ About NoorFit AI")

    st.write("""
    **NoorFit AI** is a fitness assistant built using **Streamlit**.

    Features:
    - BMI Calculator
    - Workout & Diet Plans
    - Rule-based Fitness Chatbot
    - Dashboard + Chat integration

    Runs locally and online with Streamlit Cloud.
    """)

    st.info("Built with ❤️ using Python & Streamlit")
