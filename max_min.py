#! /usr/bin/python3m

l=[3,1,1,2,0,0,2,3,3]
max_val=l[0]
min_val=l[0] #초기화 작업

for e in l:
    if e>max_val:
        max_val=e
    if e<min_val:
        min_val=e
print(f"max: {max_val}")
print(f"min: {min_val}")

l.sort()
d={}
for x in l:
    if x in d:
        d[x]=+1
    else:
        d[x]=1
print(d) #34) 
