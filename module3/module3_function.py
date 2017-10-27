#!flask/bin/python
import sys
import json
import datetime

def get_module3_sample1(required_par1,required_par2):
    return_data = {}
    return_data['request_utctime'] = datetime.datetime.utcnow()
    return_data['request_function'] = 'module3_sample1'
    return_data['required_par1'] = required_par1
    return_data['required_par2'] = required_par2
    return return_data

def get_module3_sample2(required_par1,required_par2):
    return_data = {}
    return_data['request_utctime'] = datetime.datetime.utcnow()
    return_data['request_function'] = 'module3_sample2'
    return_data['required_par1'] = required_par1
    return_data['required_par2'] = required_par2
    return return_data