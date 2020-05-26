from . import main
from app.main.model import *
from flask import request, render_template

@main.route('/register', methods = ['GET', 'POST'])
def register():
    req_data = HandleHTTP.get(request)
    ret = UserInfo.save(req_data)
    ret = json.dumps(ret, ensure_ascii=False)

    return ret

@main.route('/test', methods = ['GET', 'POST'])
def test():
    return jsonify({'msg': 'success'})

