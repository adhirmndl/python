class Solution:
    def maxArea(self,A):
    	rw=0
    	a=0;b=len(A)-1
    	while a<=b:
    		rw=max(rw,abs(b-a)*min(A[a],A[b]))
    		if A[a]<A[b]:
    			a+=1
    		else:b-=1

    	return rw


a=[1, 5, 4, 3]
print Solution().maxArea(a)
