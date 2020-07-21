#! /usr/bin/python3m

import sys
"""
f=sys.argv[1]
with open(f,'r') as kk:
    for line in kk:
        if line.startswith('>'):
            continue
        for s in line.strip():
            print(s,end='')
    print()
"""

#강사님 방법

def read_txt(file_name:str)->str:
    ret = ""
    with open(file_name,'r') as kg:
        for line in kg:
            if line.startswith('>'):
                continue
            ret+=line.strip()
    return ret

if __name__=="__main__": #파이썬 밖에서 사용할 때만 돌아가게끔
    if len(sys.argv)!=2:
        print(f"#usage : python {sys.argv[0]} [txt]")
        sys.exit()
    file_name=sys.argv[1]
    txt=read_txt(file_name)
    print(txt)
