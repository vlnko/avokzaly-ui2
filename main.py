from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html", page_title="Index")


@app.route("/passengers")
def passengers_page():
    return render_template("passengers.html", page_title="Passengers")


@app.route("/success")
def success_page():
    return render_template("success.html", page_title="Success page")


@app.route("/my-tickets")
def my_tickets_page():
    return render_template("my-tickets.html", page_title="My tickets")


@app.route("/trips")
def trips_page():
    return render_template("trips.html", page_title="Trips")


if __name__ == '__main__':
	app.run(debug=False)