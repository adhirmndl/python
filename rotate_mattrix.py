class Solution:
    # @param A : list of integers
    # @return a list of integers
    def rotate(self,A):
    	A=A[::-1]
    	k=[]
    	for i in range(len(A)):
    		l=[]
    		for j in range(len(A[0])):
    			l.append(A[j][i])
    		k.append(l)
    	return k


o=[[1,2,3],[4,5,6],[7,8,9]]
o=[[1, 2],[3, 4]]
print Solution().rotate(o)