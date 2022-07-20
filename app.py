from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "806e92b2fd082c4b3bbcad60722de1a6"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return redirect("/")

    data = request.form
    email = data["email"]
    message = data["message"]

    with open("contact-details.txt", "a") as f:
        string = f"email: {email} message: {message}\n"
        f.write(string)

    flash("We received your message. We will get in touch shortly", "success")
    return redirect("/")


if __name__ == "__main__":
    app.run()