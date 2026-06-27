from flask import Flask, request

app = Flask(__name__)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"


@app.route("/", methods=["GET", "POST"])
def home():
    result_html = ""
    weight_value = ""
    height_value = ""

    if request.method == "POST":
        weight_value = request.form.get("weight", "")
        height_value = request.form.get("height", "")

        try:
            weight = float(weight_value)
            height = float(height_value)

            if weight <= 0 or height <= 0:
                result_html = "<p>Please enter positive values for weight and height.</p>"
            else:
                bmi = weight / (height ** 2)
                category = get_bmi_category(bmi)
                result_html = f"""
                <section>
                    <h2>BMI Calculator Result</h2>
                    <p>Your BMI is: {bmi:.2f}</p>
                    <p>You are classified as: {category}</p>
                    <a href="/">Calculate Again</a>
                </section>
                """
        except ValueError:
            result_html = "<p>Please enter valid numbers for weight and height.</p>"

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>BMI Calculator</title>
    </head>
    <body>
        <h1>BMI Calculator</h1>
        <form method="POST">
            <label for="weight">Weight in kilograms:</label>
            <input type="number" id="weight" name="weight" step="0.01" min="0.01" value="{weight_value}" required>
            <br>
            <label for="height">Height in meters:</label>
            <input type="number" id="height" name="height" step="0.01" min="0.01" value="{height_value}" required>
            <br>
            <button type="submit">Calculate BMI</button>
        </form>
        {result_html}
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
