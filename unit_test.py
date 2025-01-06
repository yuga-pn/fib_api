import pytest
import main_app
import subprocess
import pycurl


curl_command = [
    "curl",
    "-X", "GET",
    "https://fib-api-bwwo.onrender.com/"
]
default_page = "https://fib-api-bwwo.onrender.com/"
fib = "fib?n="
test_cases = ["","10","2","1","0","w","10w","1000","99999"]

def use_exsample(test_case):
    for case in test_cases:
        inputs = default_page + fib + case
        curl_command[3] = inputs
        result = subprocess.run(curl_command, capture_output=True, text=True)
        # 結果を出力
        print("Response code:" , inputs)
        print("Response body:", result.stdout)

use_exsample(test_cases)
