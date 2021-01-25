from flask import Flask, send_from_directory

app = Flask("Example 1")

@app.route("/")
def index():
    return send_from_directory(
        "html",
        filename = "home.html")

@app.route("/about")
def about():
    return send_from_directory(
        "html",
        filename = "about.html")

app.run()
