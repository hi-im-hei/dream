from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flaskbook"

@app.route("/hello")
def hello():
    return "Hello, hi_im_hei"