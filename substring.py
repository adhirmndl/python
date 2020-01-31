a=[0,1,2,3,4,5,6,7,8,9]
for i in range(len(a)):
	m=0;
	for j in range(i+1):
		print (a[m:len(a)-i+m])
		m+=1
	print ("")
