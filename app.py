# app.py
from flask import Flask, render_template, request
from why_solver import why_theory_solver  # import your solver logic

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        problem = request.form["problem"]
        result = why_theory_solver(problem)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
