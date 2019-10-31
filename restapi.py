import json
from flask import Flask,jsonify,request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
@app.route("/api/add",methods=["POST"])
def addtwo():
    num1=request.json["number1"]
    num2=request.json["number2"]
    sum=int(num1)+int(num2)
    object={"sum":sum}
    json_object=jsonify(object)
    return json_object

if __name__ == "__main__":
    app.run(port=8080)
