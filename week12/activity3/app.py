from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Learn Flask</title>
        <style>
            h1 {
                font-family: Georgia, "Times New Roman", serif;
                font-style: italic;
            }
        </style>
    </head>
    <body style="background-color: green; color: red;">
        <h1>Flask Quickstart</h1>
        <p>
            Visit the
            <a href="https://flask.palletsprojects.com/en/stable/quickstart/">
                Flask Quickstart documentation
            </a>
            to learn more about Flask.
        </p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)
