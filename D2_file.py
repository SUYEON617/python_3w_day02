#! /usr/bin/python3m

import sys
import gzip #gzip 사용할 수 있게끔


if len(sys.argv)!=2:
    print(f"#usage : python {sys.argv[0]} [fasta.gz]")
    sys.exit()
    
f=sys.argv[1]
d={}

with gzip.open(f,'rb') as kk: #rb means read binary
    for line in kk:
        line = line.decode("utf-8") #바이트 형식을 utf로 바꿔서 string으로 볼 수 있게끔
#        print(line.strip())
        if line.startswith('>'):
            continue
        for s in line.strip():
            if s in d:
                d[s]+=1
            else:
                d[s]=1

print(d)

with open("covid_result_day2.txt",'w') as o:
    o.write(f"A: {d['A']}\n")
    o.write(f"T: {d['T']}\n")
    o.write(f"C: {d['C']}\n")
    o.write(f"G: {d['G']}\n")
    o.write(f"전체 길이의 합 : {d['A']+d['T']+d['C']+d['G']}")
