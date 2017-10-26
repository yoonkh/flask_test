from flask import Flask, request

app = Flask(__name__)

searchword = request.args.get('key', '')


# ?key=Value 문자열에 접근하려면 args 속성을 사용가능하다
