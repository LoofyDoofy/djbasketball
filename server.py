
import flask
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask("__main__")

@app.route("/")
def main():
    return render_template(f"index.html")

@app.route("/people.html")
def people():
    return render_template(f"people.html")


@app.route("/events.html")
def events():
    return render_template(f"events.html")


@app.route("/askme.html")
def askme():
    return render_template(f"askme.html")


@app.route("/askmeprocessor.html",methods=["GET","POST"])
def askme_processor():
    return render_template(f"askmeprocessor.html")

if __name__ == "__main__":
    app.run("0.0.0.0",port=os.getenv('PORT'))

# os.getenv('PORT') change 80
