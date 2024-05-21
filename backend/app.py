import json
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request, make_response, jsonify
import pandas as pd
#import solution

app = Flask(__name__)
cors = CORS(app)

@app.route('/api/test', methods=['POST', 'GET'])
def get_data():
    data = {
        'message': 'Hello from Flask!'
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=9092) # 可以指定运行的主机IP地址，端口，是否开启调试模式