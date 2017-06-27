inputt = "3 1 4 6 5"
inputt="10 4 6 12 5"
arr=list(map(int,inputt.strip().split()))
arr.sort()
from collections import defaultdict
d=defaultdict(bool)
for i in arr:
	d[i**2]=True
k=-1
for i in range(len(arr)):
	if k!=-1:break
	for j in range(i+1,len(arr)):
		if d[arr[i]**2+arr[j]**2]:
			k=1;print True
			break
if k==-1:print False