from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# import os

# Init app
app = Flask(__name__)


# Delete Product
def x(s,s1,s2):
  product={"api":"successful",
           "Invoice":s,
           "date":s2,
           "amt":s1
           }
  return product

def Product(s,s1,s2,s3):
  product={"api":s3,
           "Invoice":s,
           "date":s2,
           "amt":s1
           }
  return product



@app.route('/')
def index():
    headers = request.headers
    auth = headers.get("Api-Key")
    if auth == 'ashu':
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401


# @app.route("/", methods=['GET','POST'])
# def new():
#   user = request.args.get('data')
#   u=user.split(".")
#   print(u)
#
#
#   return jsonify(x(u[0],u[1],u[2]))



@app.route('/api', methods=['GET', 'POST'])
def add_message():
    content = request.json
    c=content['mytext']
    return jsonify({"name":c})

# Run Server
if __name__ == '__main__':
  app.run(debug=True,threaded=True)