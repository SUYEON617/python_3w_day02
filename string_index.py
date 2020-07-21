#! /usr/bin/python3m
#30번

"""
seq1='AGTTTATAG'
print(seq1)

for i in range(1,len(seq1)+1,1):
    if seq1[i:i+2] =='TT':
        print(i)
"""


#강사님 방법

import sys

seq=sys.argv[1]

for i in range(0,len(seq),1):
    if seq[i:i+2]=='TT':
        print(i)
