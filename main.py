from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html", page_title="Index")


@app.route("/passengers")
def passengers_page():
    return render_template("passengers.html", page_title="Passengers")


if __name__ == '__main__':
	app.run(debug=False)