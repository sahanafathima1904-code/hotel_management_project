from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary booking storage
bookings = []

# Login details
USERNAME = "admin"
PASSWORD = "1234"


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("index.html", bookings=bookings)


@app.route("/book", methods=["POST"])
def book():

    guest_name = request.form["guest_name"]
    email = request.form["email"]
    check_in = request.form["check_in"]
    check_out = request.form["check_out"]
    room = request.form["room"]

    booking = {
        "guest_name": guest_name,
        "email": email,
        "check_in": check_in,
        "check_out": check_out,
        "room": room,
        "status": "Confirmed"
    }

    bookings.append(booking)

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)