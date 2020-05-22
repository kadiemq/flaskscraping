from concurrent.futures.thread import ThreadPoolExecutor

from flask import Blueprint, request, jsonify

from functions.fn_User import function_RegisterUser, function_Login

UserRegisterApi_Router = Blueprint('router1', __name__)
UserLoginApi_Router = Blueprint('router2', __name__)


# /a_api
@UserRegisterApi_Router.route('/', methods=['POST'])
def index():
    email = request.json['email']
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    password = request.json['password']

    executor = ThreadPoolExecutor()
    t = executor.submit(function_RegisterUser, email, first_name, last_name, password)
    response = t.result()

    return jsonify(response)


@UserLoginApi_Router.route('/', methods=['POST'])
def index():
    ip_address = request.remote_addr
    email = request.json['email']
    password = request.json['password']
    print(f"Address: {ip_address}")

    executor = ThreadPoolExecutor()
    t = executor.submit(function_Login, email, password)
    response = t.result()

    return jsonify(response)
