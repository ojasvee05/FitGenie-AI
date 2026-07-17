from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# BMI + Water Intake + Calorie Calculator
@app.route("/calculate", methods=["POST"])
def calculate():

    # User Input
    name = request.form["name"]
    age = int(request.form["age"])
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    gender = request.form["gender"]
    goal = request.form["goal"]

    # BMI Calculation
    height_m = height / 100
    bmi = weight / (height_m * height_m)
    bmi = round(bmi, 2)

    # Water Intake Calculation
    water_ml = weight * 35
    water_litre = round(water_ml / 1000, 1)

    # Calorie Calculation (Mifflin-St Jeor Formula)
    if gender == "Male":
        calories = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        calories = 10 * weight + 6.25 * height - 5 * age - 161

    if goal == "Weight Loss":
        calories -= 300
    elif goal == "Weight Gain":
        calories += 300

    calories = round(calories)

    # Diet Recommendation
    if goal == "Weight Loss":
        diet = [
            "🥣 Breakfast: Oats + Milk + Apple",
            "🍛 Lunch: 2 Roti + Dal + Salad",
            "🥜 Evening Snack: Roasted Chana",
            "🍽 Dinner: Paneer + Vegetables"
        ]

    elif goal == "Weight Gain":
        diet = [
            "🥛 Breakfast: Banana Shake + Peanut Butter",
            "🍚 Lunch: Rice + Dal + Paneer",
            "🥜 Evening Snack: Dry Fruits",
            "🍽 Dinner: Chapati + Soya Chunks"
        ]

    else:
        diet = [
            "🥣 Breakfast: Poha + Milk",
            "🍛 Lunch: Dal + Rice + Vegetables",
            "🍎 Evening Snack: Fruits",
            "🍽 Dinner: Chapati + Paneer"
        ]
        # Workout Recommendation
    if goal == "Weight Loss":
        workout = [
            "🏃 30 min Running",
            "🚴 20 min Cycling",
            "🔥 HIIT Workout (15 min)",
            "🧘 10 min Stretching"
        ]

    elif goal == "Weight Gain":
        workout = [
            "🏋️ Weight Training",
            "💪 Compound Exercises",
            "🥇 Progressive Overload",
            "🚶 15 min Walking"
        ]

    else:
        workout = [
            "🚶 30 min Walking",
            "🏋️ Full Body Workout",
            "🧘 Yoga",
            "🤸 Stretching"
        ]

        # Sleep Recommendation
    if goal == "Weight Loss":
        sleep = "😴 7-8 hours of quality sleep."

    elif goal == "Weight Gain":
        sleep = "😴 8-9 hours for better muscle recovery."

    else:
        sleep = "😴 Maintain 7-8 hours of sleep daily."

    # BMI Category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    return render_template(
        "result.html",
        name=name,
        bmi=bmi,
        category=category,
        water=water_litre,
        calories=calories,
        diet=diet,
        workout=workout,
        sleep=sleep
    )


if __name__ == "__main__":
    app.run(debug=True)