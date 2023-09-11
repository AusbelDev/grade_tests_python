from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["UPLOAD_FOLDER"] = "static/images/"


@app.route("/")
def index():
    # return the index.html file
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    filename: str = file.filename if file.filename else ""
    file.save(os.path.join(basedir, app.config["UPLOAD_FOLDER"], filename))
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
