from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Carl — Why Theory Solver is live on Render!"

