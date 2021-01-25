from flask import Flask, render_template

app = Flask("Exercise 1")

logged_in = False

@app.route("/")
def index():
    return render_template(
        "exercise1.html")

app.run()