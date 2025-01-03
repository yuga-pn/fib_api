from flask import Flask,request, jsonify
import math

def calc_fib(n):
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

def number_judge(inputs):
    try:
        n = int(inputs)
    except ValueError:
        return False
    else:
        return True
    
def float_judge(inputs):
    try:
        n = float(inputs)
    except ValueError:
        return False
    else:
        return True
def assignment(inputs):
    judge_number = number_judge(inputs)
    #入力が数値か判断する
    if(judge_number == True):
        n = int(inputs)
        if(n > 0):
            fib_sequence = calc_fib(n)
            if(math.log10(fib_sequence) <= 4300):#intをstrに変換できる桁数の上限が4300桁
                return 200, "ok",fib_sequence
            else:
                return 400, "The entered number is too large to display.",0
        else:
            return 400, "Input must be over 0",0
    else:#入力が数値でない
        judge_float = float_judge(inputs)
        if(judge_float):
            return 400, "Input must be integer",0
        else:
            return 400, "Input must be number",0


