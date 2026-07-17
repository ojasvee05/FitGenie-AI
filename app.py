from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# BMI Calculator
@app.route("/calculate", methods=["POST"])
def calculate():

    name = request.form["name"]
    height = float(request.form["height"])
    weight = float(request.form["weight"])

    height = height / 100
    bmi = weight / (height * height)
    bmi = round(bmi, 2)
    water_ml = weight *35
    water_litre = round(water_ml /1000, 1)

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
        water=water_litre
    )

if __name__ == "__main__":
    app.run(debug=True)