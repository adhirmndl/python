class Solution:
    def findMedian(self,A):
    	a=[]
    	for i in range(A):
    		for k in i:
    			a.append(k)
    	a.sort()
    	return a[int(len(a)/2)]




A = [[1, 2, 3], [3, 5, 6], [6, 9, 9]]
print Solution().findMedian(A)