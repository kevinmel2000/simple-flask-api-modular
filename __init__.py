#!flask/bin/python
import sys
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask_cors import CORS

app = Flask(__name__, static_folder='/srv/static')
cors = CORS(app, resources={r"/files/*": {"origins": "*"}})

# start import from modules
# module1
from module1.module1_route import module1_api
app.register_blueprint(module1_api)
# module2
from module2.module2_route import module2_api
app.register_blueprint(module2_api)
# module3
from module3.module3_route import module3_api
app.register_blueprint(module3_api)
# end im from modules
    
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

@app.errorhandler(405)
def not_found(error):
    return make_response(jsonify( { 'error': 'Method Not Allowed' } ), 405)

@app.errorhandler(500)
def not_found(error):
    return make_response(jsonify( { 'error': 'Internal Server Error' } ), 500)

@app.route('/files/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug = True)
