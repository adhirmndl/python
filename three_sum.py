class Solution:
    def threeSumClosest(self,A,B):
    	l=[]
    	for i in range(len(A)):
    		for j in range(len(A)):
    			
    	'''t=9999999999999
    	sm=0
    	for i in range(len(A)):
    		for j in range(i+1,len(A)):
    			for k in range(j+1,len(A)):
    				c=A[i]+A[j]+A[k]
    				if t>abs(B-c):
    					t=abs(B-c)
    					sm=c
    			
    	return sm'''
    	




a=[-1, 2, 1, -4]
b=2
#a=[ -4, -8, -10, -9, -1, 1, -2, 0, -8, -2 ]
#b=0
a= [ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
b=-1
print Solution().threeSumClosest(a,b)
