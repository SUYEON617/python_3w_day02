#! /usr/bin/python3m

import sys
"""
f=sys.argv[1]
d={}
with open(f,'r') as kk:
    for line in kk:
        if line.startswith('>'):
            continue
        for s in line.strip():
            if s in d:
                d[s]+=1
            else:
                d[s]=1

print(d)

for x in d.keys():
    print(f"{x}는 {d[x]}개")
"""
#강사님 풀이

class FASTA:
    def __init__(self,file_name:str):
        self.file_name=file_name
        self.count={}
        self.length=0
    def count_base(self):
        with open(self.file_name,'r') as k:
            for line in k:
                if line.startswith('>'):
                    continue
                line=line.strip()
                for s in line:
                    if s in self.count:
                        self.count[s]+=1
                    else:
                        self.count[s]=1
    def get_length(self):
        for k,v in self.count.items():
            self.length+=v
    def __len__(self):
        self.get_length()
        return self.length

if __name__=="__main__":
    if len(sys.argv) !=2:
        print(f"#usage : python {sys.argv[0]} [fasta]")
        sys.exit()
    file_name=sys.argv[1]
    t=FASTA(file_name)
    t.count_base()
    print(t.count)
    t.get_length()
    print(t.length)
