from flask import Flask,request, jsonify
from application import fib_app
import math

app = Flask(__name__)

@app.route("/fib",methods=['GET'])
def assignment():
    inputs = request.args.get("n","non_input") #!入力されなかった場合の処理
    judge_number = fib_app.number_judge(inputs)
    if(inputs == "non_input"):
        return jsonify({"status": 400, "message": "Please enter number!"}), 400
    #入力が数値か判断する
    if(judge_number == True):
        #judge_integer = float(inputs).is_integer
        #入力が整数か判断する
        #if(judge_integer == True):
            n = int(inputs)
            if(n > 0):
                fib_sequence = fib_app.calc_fib(n)
                if(math.log10(fib_sequence) <= 4300):#intをstrに変換できる桁数の上限が4300桁
                    return jsonify({"result": fib_sequence}), 200
                else:
                    return jsonify({"status": 400, "message": "The entered number is too large to display."}), 400
            else:
                return jsonify({"status": 400, "message": "Input must be over 0"}), 400
        #else:
            #return jsonify({"status": 400, "message": "Input must be integer"}), 400
    else:#入力が数値でない
        return jsonify({"status": 400, "message": "Input must be number"}), 400

@app.route("/")
def welcome():
    return "<p>Welcome to my server! This server calculates fibonacchi sequence. Please enter number you want to know.</p>"