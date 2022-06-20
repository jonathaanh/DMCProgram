from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from pdfCalculator import pdfCalculator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("calculate.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    print("Get a request")
    if request.method == "POST":
        # a = request.form.get('a')
        # b = request.form.get('b')
        #print(request.data)
        content = request.json
        a = content['a']
        b = content['b']
        
        #print(request.form.get('b'))
        #print(a)
        #print(b)
        math = int(a) + int(b)
        pdf(a,b)
        #return redirect(url_for("pdf",first=a,second=b))

        return jsonify({"result": str(math)})
        
def pdf(a,b):
    math = int(a) + int(b)
    pdfCalc = pdfCalculator()
    pdfCalc.add(a,b)
    return pdfCalc.add(a,b)

if __name__ == "main":
    app.run(debug=True)