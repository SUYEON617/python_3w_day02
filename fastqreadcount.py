#! /usr/bin/python3m

import sys
"""
f=sys.argv[1]
d=0
o=[]
with open(f,'r') as kk:
    for line in kk:
#        if line.startswith('@'):
#            d+=1
#print(d)
        line=line.replace('\n','')
        o.append(line)
print(o)
print(len(o)//4)
"""
#강사님 풀이 

class FASTQ:
    def __init__(self,file_name):
        self.file_name=file_name
        self.read_num=0
    def count_read(self):
        cnt=0
        with open(self.file_name,'r') as k:
            for line in k:
                if cnt%4==0:
                    header=line.strip()
                    self.read_num+=1 #어디에 넣든 상관 없음. 그냥 헤더면 1더해주는 걸로 갔다.
                elif cnt%4==1:
                    seq=line.strip()  
                elif cnt%4==3:
                    qual=line.strip()
                cnt+=1

if __name__=="__main__":
    if len(sys.argv) !=2:
        print(f"usage : python {sys.argv[0]} [fastq]")
        sys.exit()
    file_name=sys.argv[1]
    t=FASTQ(file_name)
    t.count_read()
    print(t.read_num) #결과 출력
