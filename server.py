#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect, url_for
import json
from pdfCalculator import pdfCalculator

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def calculate():
    if request.method == "POST":
        a = request.form["a"]
        b = request.form["b"]
        return redirect(url_for("pdf",first=a,second=b))
    else:
        return render_template("calculate.html")


@app.route("/<first>/<second>")
def pdf(first, second): 
    pdfCalc = pdfCalculator()
    pdfCalc.calculate(first,second)
    math = int(first) + int(second)
    return f"<h1>{first} + {second} = {math}</h1>"
    
if __name__ == "main":
    app.run(debug=True)