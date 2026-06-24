import json
import hashlib
from pathlib import Path

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session
)


app = Flask(__name__)
app.secret_key = "supersecretkey"


USERS_FILE = "users.json"
TAKEN_FILE = "taken.json"


# -------------------
# Wachtwoord hashing
# -------------------

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password, password_hash):
    return hash_password(password) == password_hash


# -------------------
# Users
# -------------------

def ensure_users():

    if Path(USERS_FILE).exists():
        return

    users = [

        {
            "username": "admin",
            "password": hash_password("admin123"),
            "role": "admin"
        },

        {
            "username": "user",
            "password": hash_password("user123"),
            "role": "user"
        }

    ]

    Path(USERS_FILE).write_text(
        json.dumps(users, indent=2)
    )


def load_users():
    return json.loads(
        Path(USERS_FILE).read_text()
    )


# -------------------
# Taken
# -------------------

def load_taken():

    if not Path(TAKEN_FILE).exists():
        return []

    return json.loads(
        Path(TAKEN_FILE).read_text()
    )


def save_taken(taken):

    Path(TAKEN_FILE).write_text(
        json.dumps(taken, indent=2)
    )


# -------------------
# Login
# -------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        users = load_users()


        for user in users:

            if (
                user["username"] == username
                and check_password(
                    password,
                    user["password"]
                )
            ):

                session["user"] = user["username"]
                session["role"] = user["role"]

                return redirect("/")


        return render_template(
            "login.html",
            error="Foute login"
        )


    return render_template(
        "login.html"
    )



# -------------------
# Home
# -------------------

@app.route("/")
def index():

    if "user" not in session:
        return redirect("/login")


    taken = load_taken()


    # gewone gebruiker
    if session["role"] != "admin":

        taken = [
            t for t in taken
            if t["owner"] == session["user"]
        ]


    return render_template(
        "index.html",
        taken=taken,
        user=session["user"],
        role=session["role"]
    )



# -------------------
# Taak toevoegen
# -------------------

@app.post("/add")
def add():

    if "user" not in session:
        return redirect("/login")


    titel = request.form["titel"]


    taken = load_taken()


    taken.append({

        "titel": titel,
        "klaar": False,
        "owner": session["user"]

    })


    save_taken(taken)

    return redirect("/")



# -------------------
# Taak klaar
# -------------------

@app.get("/done/<int:i>")
def done(i):

    taken = load_taken()


    if i < len(taken):

        taken[i]["klaar"] = True

        save_taken(taken)


    return redirect("/")



# -------------------
# Delete (admin)
# -------------------

@app.get("/delete/<int:i>")
def delete(i):

    if session.get("role") != "admin":
        return redirect("/")


    taken = load_taken()


    if i < len(taken):

        taken.pop(i)

        save_taken(taken)


    return redirect("/")



# -------------------
# Logout
# -------------------

@app.get("/logout")
def logout():

    session.clear()

    return redirect("/login")



# Start

if __name__ == "__main__":

    ensure_users()

    app.run(debug=True)