from flask import Flask, request

app = Flask(__name__)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Form submitted!"
    return "Contact Form Page"