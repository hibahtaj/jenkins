from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def registration():
    return render_template("reg.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")

    return render_template("sucess.html", name=name, email=email)


if __name__ == "__main__":
    app.run(debug=True)
