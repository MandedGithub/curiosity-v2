from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/keyboardcrushermp")
def keyboardcrushermp():
    return render_template("kbcmp.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/socialmedia")
def socialmedia():
    return render_template("socialmedia.html")
