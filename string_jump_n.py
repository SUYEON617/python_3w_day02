#! /usr/bin/python3m
"""
seq1='ATGTTATAG'
print(seq1)

for i in range(1,len(seq1)+1,3):
    print(seq1[i-1:i+2]) #26)string indexing이랑 슬라이싱 되는구나

rev=seq1[::-1] #27) 문자열 뒤집기
#rev.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
d={'A':'G','T':'A','G':'C','C':'G'}
for i in rev:
    rev.replace(i,d[i])
print(rev) #28) 상보적 염기쌍

"""

#강사님 방법

import sys
def comp1(seq:str)->str:
    comp=''
    for s in seq:
        if s=='A':
            comp+='T'
        elif s=='T':
            comp+='A'
        elif s=='C':
            comp+='G'
        elif s=='G':
            comp+='C'
    return comp

def comp2(seq):
    comp=''
    d_comp={'A':'T','T':'A','G':'C','C':'G'}
    for s in seq:
        comp+=d_comp[s]
    return comp

if __name__=="__main__":
    if len(sys.argv) !=2:
        print(f"#usage: python {sys.argv[0]} [string]")
        sys.exit()
    seq=sys.argv[1]
    c1=comp1(seq)
    c2=comp2(seq)
    print(seq)
    print(c1)
    print(c2)

