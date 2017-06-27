def binS(A,s,e,v):
	print s,e,A[s:e]
	if e==s:
		if A[e]==v:
			return e
		else:
			return -1
	mid = int((s+e)/2)
	if v==A[mid]:
		return mid
	elif A[mid]>v:
		return binS(A,s,mid,v)
	else:
		return binS(A,mid+1,e,v)
A=[1,2,3,34,4,5,6,7,8,9,76,5,4,234,4,456,4575,67,457,45,46]
A.sort()
print (binS(A,0,len(A)-1,int(raw_input().strip())))