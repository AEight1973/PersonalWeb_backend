from flask import Flask, request
from flask_cors import CORS
import json
from aliyun_rds import *

'''
flask： web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务
登录接口，需要传url、username、passwd
'''
server = Flask(__name__)
CORS(server, resources=r'/*')


# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式
@server.route('/login', methods=['GET', 'POST'])
# 推荐算法主函数
def login():
    # 获取通过url请求传参的数据
    ip = request.values.get('ip')
    if request.values.get('type') == 0:
        username = 'tourist_' + ip.replace('.', '')
        password = ''
    else:
        username = request.values.get('username')
        password = request.values.get('password')

    user = Users.userinfo()
    req = user.insert(username, password, ip)

    # 返回计算完成数据
    if req:
        resume = {'code': '500000', 'message': '登陆成功'}
    else:
        resume = {'code': '500001', 'message': '登陆失败'}
    return json.dumps(resume)


@server.route('/loading', methods=['GET', 'POST'])
# 推荐算法主函数
def loading():
    # 获取通过url请求传参的数据
    page = request.values.get('page')

    # 返回计算完成数据
    resume = {'code': '500000', 'message': ''}
    return json.dumps(resume)


if __name__ == '__main__':
    server.run(debug=True, port=8808, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
