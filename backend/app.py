import json
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request, make_response, jsonify
import pandas as pd
import program

app = Flask(__name__)
cors = CORS(app)

@app.route('/api/test', methods=['POST', 'GET'])
def get_data():
    data = {
        'message': 'Hello from Flask!'
    }
    return jsonify(data)

@app.route('/api/triangle', methods=['POST', 'GET'])
def triangle():
    if request.method == 'GET':
        # 从请求中获取参数
        param1 = int(request.args.get('a'))
        param2 = int(request.args.get('b'))
        param3 = int(request.args.get('c'))


        # 调用程序
        result = program.triangle(param1, param2, param3)

    data = {
        'result': result
    }
    return jsonify(data)


@app.route('/api/computer', methods=['POST', 'GET'])
def computer():
    if request.method == 'GET':
        # 从请求中获取参数
        param1 = int(request.args.get('a'))
        param2 = int(request.args.get('b'))
        param3 = int(request.args.get('c'))

        # 调用程序
        result = program.computer(param1, param2, param3)

    data = {
        'result': result
    }
    return jsonify(data)


@app.route('/api/calendar', methods=['POST', 'GET'])
def calendar():
    if request.method == 'GET':
        # 从请求中获取参数
        param1 = int(request.args.get('a'))
        param2 = int(request.args.get('b'))
        param3 = int(request.args.get('c'))

        # 调用程序
        result = program.calendar(param1, param2, param3)

    data = {
        'result': result
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=9092) # 可以指定运行的主机IP地址，端口，是否开启调试模式