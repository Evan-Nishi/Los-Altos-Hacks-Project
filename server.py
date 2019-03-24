from flask import Flask, render_template

flask_app: Flask = Flask(__name__)

name: str = "Plant-ID"

@flask_app.route("/")
def homepage():
    return render_template("index.html", name=name)

@flask_app.route("/app")
def app():
    return render_template("app.html", name=name)

flask_app.run()
