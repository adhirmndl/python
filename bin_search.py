class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def Range(self,A,pos):
    	k=[-1,-1];p=pos;data=A[pos]
    	while pos!=-1 and A[pos]==data:
    		k[0]=pos
    		pos-=1
    	while p<len(A) and A[p]==data:
    		k[1]=p
    		p+=1
    	return k
    def binS(self,A,st,en,terget):
    	if en-st<100 and terget not in A:return [-1,-1]
    	if st==en and A[st]!=terget:
    		return [-1,-1]
    	mid=int((st+en)/2)
    	if A[mid]==terget:
    		return self.Range(A,mid)
    	elif terget>A[mid]:
    		return self.binS(A,mid,en,terget)
    	elif terget<A[mid]:
    		return self.binS(A,st,mid,terget)
    	else:
    		return [-1,-1]        
    def searchRange(self, A, B):
    	return self.binS(A,0,len(A),B)
a=[1,2,3,4,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,8,9]
a=[1]
a = [ 4, 7, 7, 7, 8, 10, 10 ]
a= [ 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10 ]
print Solution().searchRange(a,3)