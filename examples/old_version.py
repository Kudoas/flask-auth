# from flask import Flask
# from flask_jwt import JWT, jwt_required, current_identity, request, jsonify
# from werkzeug.security import safe_str_cmp
# import hashlib
# import ast


# class User(object):
#     def __init__(self, id, username, password):
#         self.id = id
#         self.username = username
#         self.password = password

#     def __str__(self):
#         return "%s" % {"id": self.id, "username": self.username, "password": self.password}


# def hash_password(password):
#     hashed_pw = hashlib.md5(password.encode()).hexdigest()
#     return hashed_pw


# # resistered users
# users = [
#     User(1, 'user1', hash_password('abcxyz')),
#     User(2, 'user2', hash_password('abcxyz')),
#     # User(3, ...)
# ]

# username_table = {u.username: u for u in users}
# userid_table = {u.id: u for u in users}


# def authenticate(username, password):
#     user = username_table.get(username, None)
#     if user and safe_str_cmp(user.password.encode('utf-8'), hash_password(password)):
#         return user


# def identity(payload):
#     user_id = payload['identity']
#     return userid_table.get(user_id, None)


# app = Flask(__name__)
# app.debug = True
# app.config['SECRET_KEY'] = 'super-secret'

# jwt = JWT(app, authenticate, identity)


# @app.route('/signup', methods=["post"])
# def signup():
#     user_info = request.get_json()
#     new_user = User(3, user_info["username"],
#                     hash_password(user_info["password"]))
#     users.append(new_user)
#     return {"message": "user created"}


# @app.route('/protected')
# @jwt_required()
# def protected():
#     return {"username": current_identity.username, "password": current_identity.password}


# if __name__ == '__main__':
#     app.run()
