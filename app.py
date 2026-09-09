from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def registration():
    return render_template("reg.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")

    return render_template("success.html", name=name, email=email)

print("poll scm")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

