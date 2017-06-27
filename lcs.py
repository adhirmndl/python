a=raw_input().strip()
b=raw_input().strip()
grid=[]
for i in range(len(b)):
	k=[0 for ii in range(len(a))]
	grid.append(k)
aa=[ 0 for i in range(len(a))]
bb=[ 0 for i in range(len(b))]
for i in range(0,len(b)):
	for j in range(len(a)):
		if a[j]==b[i]:
			grid[i][j] = max(aa[j],bb[i])+1
			aa[j]=grid[i][j]
			bb[i]=grid[i][j]
		else:
			grid[i][j] = max(aa[j],bb[i])
			aa[j]=grid[i][j]
			bb[i]=grid[i][j]
s=[]
for i in range(len(b)-1,-1,-1):
	for j in range(len(a)-1,-1,-1):
		k=grid[i][j]
		aaa=i;bbb=j;
		k1=0;k2=0;
		while k==grid[aaa][bbb] and aaa>-1 and bbb>-1:
			k1+=1
			aaa-=1;

for i in grid:
	print i
print ("------")
print aa,bb