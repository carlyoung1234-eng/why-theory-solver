from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ask")
def ask():
    return render_template("ask.html")

@app.route("/solve", methods=["POST"])
def solve():
    question = request.form.get("question")
    mode = request.form.get("mode")

    if mode == "quick":
        answer = f"Quick Why: {question} → a short, focused response."
    else:
        answer = f"Deep Why: {question} → a layered, expanded reasoning."

    return render_template("solve.html", question=question, answer=answer)


