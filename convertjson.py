#! /usr/bin/python3
"""
import readtxt
l=readtxt.read_tsv("read_sample.tsv")
readtxt.to_json(l)
"""

import sys
import json

def read_tsv(file_name):
    with open(file_name,'r') as k:
        ret=[]
        for line in k:
            if line.startswith('#'):
                line=line.replace('#','')
                header=line.strip().split('\t')
                continue
            splitted=line.strip().split('\t')
            d=dict(zip(header,splitted))
            ret.append(d)
    return ret

def to_json(l:list,file_name) -> None:
    with open(file_name,"w") as kk:
        json.dump(l,kk,indent=4)

if __name__=="__main__":
    if len(sys.argv) !=2:
        print(f"#usage : python {sys.argv[0]} [txt]")
        sys.exit()
    file_name=sys.argv[1]
    ret=read_tsv(file_name)
    to_json(ret)
