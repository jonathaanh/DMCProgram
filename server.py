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
        
        #return redirect(url_for("pdf",first=a,second=b))

        return jsonify({"result": str(math)})
        

# @app.route("/pdf")
# def pdf(first, second): 
#     pdfCalc = pdfCalculator()
#     pdfCalc.calculate(first,second)
#     math = int(first) + int(second)
#     return f"<h1>{first} + {second} = {math}</h1>"
    
if __name__ == "main":
    app.run(debug=True)