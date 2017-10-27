from flask import Blueprint, jsonify, abort, request, make_response, url_for
from module1_function import *

module1_api = Blueprint('module1_api', __name__)

# http://localhost:5000/module1/api/v0.1/module1_sample1
@module1_api.route('/module1/api/v0.1/module1_sample1', methods=['POST'])
def module1_sample1():
    required_pars = ['required_par1', 'required_par2']
    if not request.json or not (all(par in request.json for par in required_pars)):
        abort(400)
    value_required_par1 = request.json['required_par1']
    value_required_par2 = request.json['required_par2']
    final_data = {}
    final_data = get_module1_sample1(value_required_par1,value_required_par2)
    return jsonify(final_data)

# http://localhost:5000/module1/api/v0.1/module1_sample2
@module1_api.route('/module1/api/v0.1/module1_sample2', methods=['POST'])
def module1_sample2():
    required_pars = ['required_par1', 'required_par2']
    if not request.json or not (all(par in request.json for par in required_pars)):
        abort(400)
    value_required_par1 = request.json['required_par1']
    value_required_par2 = request.json['required_par2']
    final_data = {}
    final_data = get_module1_sample2(value_required_par1,value_required_par2)
    return jsonify(final_data)