from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name")
    age = request.form.get("age")
    return render_template("greeting.html", name=name, age=age)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)