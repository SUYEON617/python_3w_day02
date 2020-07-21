#! /usr/bin/python3m
"""
f=open('./read.txt','r')
for i in f.readlines():
    print(i.strip())
f.close()
"""


#강사님 방법
import sys
if len(sys.argv) !=2:
    print(f"#usage : python {sys.argv[0]} [fasta file]") #파일을 안 넣었을 때 오류 메시지
    sys.exit() 

f= sys.argv[1]
d={}

try:
    with open(f,'r') as kk:
        for line in kk:
            if line.startswith('>'):
                continue #출력안되고 지나가게끔
#           print(line.strip()) #기본적으로 print에서와 원래 문서의 엔터가 두번 엔터가 있어서 이걸 없애주는 것
            for s in line.strip():
                if s in d:
                    d[s]+=1
                else:
                    d[s]=1
except FileNotFoundError:
    print(f"{f} is not found.. please check one more time")
    sys.exit()

print(d) 
total=0
print(d.items())
for k,v in d.items():
    total+=v
print(total) #전체 염기서열 길이 확인.

#--------------------------------       

with open("COVID.txt",'w') as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"G: {d['G']}\n")
    handle.write(f"T: {d['T']}\n")
    handle.write(f"C: {d['C']}\n")
