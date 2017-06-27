class Solution:
    def maxArea(self,A,B):
    	rw=0
    	a=0;b=len(A)-1
    	for i in range(len(A)):
    		for j in range(i+1,len(A)):
    			if abs(A[i]-A[j])==B:
    				return 1
    	return -1


a=[1, 5, 4, 3]
a=[1, 3, 5]
b=4
print Solution().maxArea(a,b)