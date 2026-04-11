from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    posts = ["First Post", "Second Post"]
    return render_template("index.html", posts=posts)