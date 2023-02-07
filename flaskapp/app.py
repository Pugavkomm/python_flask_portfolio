from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def default():
    return render_template("default.html", name="Mechislav")


@app.route("/work")
def work():
    return render_template("work.html", name="Work")


if __name__ == "__main__":
    app.run(debug=True)
