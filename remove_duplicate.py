class Solution:
    def removeElement(self, A):
    	if len(A)==0:return 0
    	elif len(A)==1:return 1

    	a=0
    	a=A[0]
    	for i in range(1,len(A)):
    		if A[a]!=A[i]:
    			A[a+1]=A[i]
    			a+=1
    	return a
a=[1,2,3,3,3,3,3,3,4,7,5,6]
print Solution().removeElement(a)