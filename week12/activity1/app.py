from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_flask():
    return "<p>Hello, Flask!</p>"


@app.route("/bye")
def bye():
    return "<p>Bye, Flask!</p>"


@app.route("/username/<name>")
def learn(name):
    return f"{name} is learning Flask!"


@app.route("/<name>/<int:number>")
def learn_time(name, number):
    return f"{name} is learning Flask! She wakes up at {number} a.m. every day!"


if __name__ == "__main__":
    app.run(debug=True)
