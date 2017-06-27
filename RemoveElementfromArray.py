class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
    	a=[]
    	for i in range(len(A)-1,-1,-1):
    		if B==A[i]:
    			a.append(i)
    	for i in a:
    		del A[i]
    	return A


a= [4, 1, 1, 2,2,2,2, 1, 3]
print Solution().removeElement(a,2)