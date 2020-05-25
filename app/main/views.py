from . import main
from app.main.model import *
from flask import request, jsonify

@main.route('/hello', methods = ['GET', 'POST'])
def hello():

    return jsonify({'msg': 'Hello'})
