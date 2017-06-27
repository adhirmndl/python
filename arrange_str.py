s=raw_input()
from collections import defaultdict
d=defaultdict(int)
for i in s:
	d[i]+=1;
sm=0
for i in d:
	sm+=d[i]
k=True;
for i in d:
	if sm-d[i]<d[i]-1:
		k=False
		break
print 1 if k else 0