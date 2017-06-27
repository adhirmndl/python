class Solution:
    # @param A : integer
    # @return a list of list of integers
    def hotel(self,A,B,k):
    	A.sort()
    	B.sort()
    	a=A[::-1]
    	b=B[::-1]
    	s=0
    	while len(a):
    		#print a,b,s
    		if a[-1]<b[-1]:
    			a.pop()
    			#print "a poped"
    			if 1+s>k:
    				return 0
    			else:
    				s+=1
    		else:
    			b.pop()
    			s-=1
    			#print "b poped"
    		
    	return 1



print Solution().hotel([11, 24, 36, 15, 16, 23, 20, 19 ],[14, 32, 67, 25, 21, 54, 61, 34 ],4)