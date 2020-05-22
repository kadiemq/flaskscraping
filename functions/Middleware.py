from functools import wraps

import jwt
from flask import g

from methods.DatabaseMethods.DoExist import DoExist
from methods.DatabaseMethods.GetOneDB import GetOneDB


# TODO Check date verification
def middleware_CheckUser(req):
    def middleware(f):
        @wraps(f)
        def _middleware(*args, **kwargs):
            print(req.environ['REMOTE_ADDR'], req.remote_addr)
            public_key = open("public_key", "r").read().encode('utf8')

            try:
                token = req.json['token']
            except TypeError:
                g.logged_in = False
                g.is_admin = False
                g.message = 'There is no token'
                return g.message

            try:
                data = jwt.decode(token, public_key, algorithms='RS256')
            except:
                g.logged_in = False
                g.is_admin = False
                g.message = 'There is an error with your token.'
                return g.message

            email = data['email']

            if not DoExist('account', email):
                g.logged_in = False
                g.is_admin = False
                g.message = 'There is an error with your token.'
                return g.message

            user = GetOneDB('account', 'email', email)
            is_admin = user['is_admin']
            g.is_admin = is_admin
            g.logged_in = True

            return f(*args, **kwargs)

        return _middleware

    return middleware
