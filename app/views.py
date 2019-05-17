from flask import Blueprint, render_template, request, redirect, url_for, Response
from .myredis import *
from .structure import ReturnValue
from .utils import resposta
from flask import jsonify
import json

app_ = Blueprint('app_', __name__)
REDIS = MyRedis()


@app_.route('/<key>', methods=['GET'])
def get_value(key):
    status = REDIS.get_value(key)
    return resposta(True, status, 200)


@app_.route('/<key>', methods=['PUT'])
def change_value(key):
    try:
        value = request.json['value']
    except:
        return resposta(
            False,
            'You must inform value to input in key %s. Accepetd format: "value=[a-zA-Z0-9-_]"'
            % key, 405)
    if REDIS.get_value(key) != ReturnValue.NIL_:
        status = REDIS.set_value(key, value)
        return resposta(True, status, 200)
    else:
        return resposta(
            False, "You must use method POST to add new values.", 405)


@app_.route('/<key>/<extime>', methods=['PUT'])
def change_value_with_extime(key, extime):
    try:
        value = request.json['value']
    except:
        return resposta(
            False,
            'You must inform value to input in key %s. Accepetd format: "value=[a-zA-Z0-9-_]"'
            % key, 405)
    if REDIS.get_value(key) != ReturnValue.NIL_:
        status = REDIS.set_value(key, value, extime)
        return resposta(True, status, 200)
    else:
        return resposta(
            False, "You must use method POST to add new values.", 405)


@app_.route('/<key>', methods=['POST'])
def set_value(key):
    try:
        value = request.json['value']
    except:
        return resposta(
            False,
            'You must inform value to input in key %s. Accepetd format: "value=[a-zA-Z0-9-_]"'
            % key, 405)
    if REDIS.get_value(key) == ReturnValue.NIL_:
        status = REDIS.set_value(key, value)
        return resposta(True, status, 201)
    else:
        return resposta(False, "You must use method PUT to change values.", 405)


@app_.route('/<key>/<extime>', methods=['POST'])
def set_value_with_extime(key, extime):
    try:
        value = request.json['value']
    except:
        return resposta(
            False,
            'You must inform value to input in key %s. Accepetd format: "value=[a-zA-Z0-9-_]"'
            % key, 405)
    if REDIS.get_value(key) == ReturnValue.NIL_:
        status = REDIS.set_value(key, value, extime)
        return resposta(True, status, 201)
    else:
        return resposta(False, "You must use method PUT to change values.", 405)


@app_.route('/', methods=['DELETE'])
def delete_value():
    value = request.json['value']
    status = REDIS.delete_value(value)
    return resposta(True, status, 200)


@app_.route('/size', methods=['GET'])
def size():
    status = REDIS.dbSize()
    return resposta(True, status, 200)


@app_.route('/incr/<key>', methods=['PUT'])
def incr_value(key):
    status = REDIS.incr(key)
    return resposta(True, status, 200)


@app_.route('/zadd/<key>', methods=['POST'])
def zadd_value(key):
    value = request.json['value']
    status = REDIS.zadd(key, value)
    return resposta(True, status, 200)


@app_.route('/zcard/<key>', methods=['GET'])
def zcard_value(key):
    status = REDIS.zcard(key)
    return resposta(True, status, 200)


@app_.route('/zrank/<key>', methods=['GET'])
def zrank_value(key):
    try:
        value = request.json['value']
    except:
        value = None
    status = REDIS.zrank(key, value)
    return resposta(True, status, 200)


@app_.route('/zrange/<key>/start/<start>/end/<end>', methods=['GET'])
def zrange_value(key, start, end):
    try:
        start = int(start)
        end = int(end)
    except ValueError:
        return resposta(
            True, "both values, start and end, must be integer type.", 200)

    status = REDIS.zrange(key, start, end)

    return resposta(True, status, 200)
