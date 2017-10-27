from flask import Blueprint, jsonify, abort, request, make_response, url_for
from module2_function import *

module2_api = Blueprint('module2_api', __name__)

# http://localhost:5000/module2/api/v0.1/module2_sample1
@module2_api.route('/module2/api/v0.1/module2_sample1', methods=['POST'])
def module2_sample1():
    required_pars = ['required_par1', 'required_par2']
    if not request.json or not (all(par in request.json for par in required_pars)):
        abort(400)
    value_required_par1 = request.json['required_par1']
    value_required_par2 = request.json['required_par2']
    final_data = {}
    final_data = get_module2_sample1(value_required_par1,value_required_par2)
    return jsonify(final_data)

# http://localhost:5000/module2/api/v0.1/module2_sample2
@module2_api.route('/module2/api/v0.1/module2_sample2', methods=['POST'])
def module2_sample2():
    required_pars = ['required_par1', 'required_par2']
    if not request.json or not (all(par in request.json for par in required_pars)):
        abort(400)
    value_required_par1 = request.json['required_par1']
    value_required_par2 = request.json['required_par2']
    final_data = {}
    final_data = get_module2_sample2(value_required_par1,value_required_par2)
    return jsonify(final_data)