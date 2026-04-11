from flask import Flask, request

app = Flask(__name__)
users = []

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    users.append(username)
    return f"User {username} registered!"