＜コード構成＞
fib_api - main_app.py
        - requirements.txt
        - unit_test.py
        - applications
            - fib_app.py

＜概要＞
HTTPリクエストにより数値が入力され、フィボナッチ数列のその順番目の値を出力する。未入力、文字列を含む入力、小数、0以下の入力に対してはエラーを出力する。またPythonでint型をstr型に変換できる桁数の上限が4300桁であるため、表示する値が4300桁を超える場合にもエラーを出力する。
