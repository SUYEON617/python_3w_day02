#! /usr/bin/python3m
import sys
f=sys.argv[1]


#dict(zip(list1,list2)) -> 두개의 리스트가 키 , value인 딕셔너리로 넣어줌

def read_csc(file_name: str)->list:
    with open(f,'r') as kk:
        ret=[]
        for line in kk:
            if line.startswith('#'):
                line=line.replace('#','')
                header=line.strip().split(',')
                continue
            splitted=line.strip().split(',')
            d=dict(zip(header,splitted))
            ret.append(d)
    return ret

print(read_csc(f))
