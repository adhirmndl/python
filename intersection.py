class Solution:
    def intersection(self,A,B):
    	A.sort()
    	B.sort()
    	a=b=0;
    	k=[]
    	while a<len(A) and b<len(B):
    		if A[a]<B[b]:
    			a+=1
    		elif A[a]>B[b]:
    			b+=1
    		else:
    			k.append(A[a])
    			a+=1;b+=1;
    	return k




a=[1, 2, 3, 3, 4, 5, 6]
b=[3, 3, 5]
print Solution().intersection(a,b)
