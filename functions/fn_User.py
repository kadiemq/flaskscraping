from datetime import datetime, timezone, timedelta

import jwt

from classes.User import User
from methods.DatabaseMethods.DoExist import DoExist
from methods.DatabaseMethods.GetOneDB import GetOneDB
from methods.DatabaseMethods.InsertDB import InsertDB


def function_RegisterUser(email, first_name, last_name, password):
    if DoExist('account', email):
        return 'Account is already registered.'

    user = User(email, first_name, last_name)
    user.password = password

    userId = InsertDB('account', user)
    return userId


def function_Login(email, password):
    if not DoExist('account', email):
        return 'No account is registered with that email'

    data = GetOneDB('account', 'email', email)

    with User(data['email'], data['first_name'], data['last_name'], data['password']) as user:
        if not user.check_password(password):
            return 'Wrong Password'

        # Gen Token
        private_key = open('private_key', 'r').read().encode('utf8')

        message = {
            'email': email,
            'iat': datetime.utcnow(),
            'exp': datetime.now(timezone.utc) + timedelta(days=1)
        }
        token = jwt.encode(message, private_key, algorithm='RS256').decode('utf8')

    return token
