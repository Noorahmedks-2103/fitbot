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
    ["Home", "BMI Calculator", "Workout Plan", "Diet Plan", "About"]
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

        st.write(f"### Your BMI is: **{bmi:.2f}**")

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

# ---------------- ABOUT ----------------
elif menu == "About":
    st.title("ℹ️ About NoorFit AI")

    st.write("""
    **NoorFit AI** is a simple fitness assistant built using **Streamlit**.

    - Beginner friendly
    - Runs locally
    - No GitHub required
    - Easy to extend with AI/ML models later
    """)

    st.info("Built with ❤️ using Python & Streamlit")
