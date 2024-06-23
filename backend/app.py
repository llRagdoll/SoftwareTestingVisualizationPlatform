import json
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request, make_response, jsonify
from test_refusejoin import run_team_test
from test_addComment import run_note_test

import program

app = Flask(__name__)
cors = CORS(app)

@app.route('/api/test', methods=['POST', 'GET'])
def get_data():
    data = {
        'message': 'Hello from Flask!'
    }
    return jsonify(data)

# T1. 判断三角形类型
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

# T4. 电脑销售问题
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

# T2. 万年历问题
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

# T13. 销售问题
def parseFloat(param):
    pass


@app.route('/api/salesCommission', methods=['POST', 'GET'])
def salesCommission():
    if request.method == 'GET':
        # 从请求中获取参数
        AS = int(request.args.get('AS'))*10000
        LD = int(request.args.get('LD'))
        CCR = float(request.args.get('CCR'))

        # 调用程序
        CV = program.calculate_commission(AS, LD, CCR)

        if CV==-1:
            pass;
        else:
            CV = CV*0.0001
            CV=round(CV, 2)

    data = {
        'result': CV
    }
    return jsonify(data)


# T7. 电信收费问题
@app.route('/api/telecom', methods=['POST', 'GET'])
def telecomCharge():
    if request.method == 'GET':
        # 从请求中获取参数
        param1 = int(request.args.get('time'))
        param2 = int(request.args.get('count'))

        # 调用程序
        result = program.telecom(param1, param2)

    data = {
        'result': result
    }
    return jsonify(data)


@app.route('/api/teamsystem', methods=['POST', 'GET'])
def teamsystem():

    # 调用程序
    result = run_team_test()

    data = {
        'result': result
    }
    return jsonify(data)



@app.route('/api/notesystem', methods=['POST', 'GET'])
def notesystem():
        # 调用程序
        result = run_note_test()
    
        data = {
            'result': result
        }
        return jsonify(data)

if __name__ == '__main__':
    app.run(port=9092) # 可以指定运行的主机IP地址，端口，是否开启调试模式