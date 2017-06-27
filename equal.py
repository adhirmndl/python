class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
    	from collections import defaultdict
    	d=defaultdict(list)
    	for i in range(len(A)):
    		for j in range(i+1,len(A)):
    			if len(d[i+j])==0: d[i+j] = [i,j]
    	for i in d:
    		print d[i]











a=[3, 4, 7, 1, 2, 9, 8]
print Solution().equal(a)