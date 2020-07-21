#! /usr/bin/python3m
import json
def read_json(file_name:str)->list:
    with open(file_name,'r') as kk:
        l=json.load(kk)
    return l
