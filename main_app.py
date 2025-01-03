from flask import Flask,request, jsonify
from application import fib_app
import math
from dotenv import load_dotenv
from waitress import serve

app = Flask(__name__)

@app.route("/fib",methods=['GET'])
def fibonacchi():
    inputs = request.args.get("n","non_input") #!入力されなかった場合の処理
    if(inputs == "non_input"):
        return jsonify({"status": 400, "message": "Please enter number!"}), 400
    status,message,fib_sequence = fib_app.assignment(inputs)
    if(status == 200):
        return jsonify({"result": fib_sequence}), status
    else:
        return jsonify({"status": status, "message": message}), status

@app.route("/")
def welcome():
    return "<p>Welcome to my server! This server calculates fibonacchi sequence. Please enter number you want to know.</p>"

if __name__ == '__main__':
    serve(app,host="0.0.0.0",port=5000)
