class Solution:
    def convert(self,A,N):
    	S=[[] for i in range(N)]
    	k=1
    	S[0].append(A[0])
    	n=len(A)
    	
    	while k<n:
    		for i in range(1,N):
    			if k<n:
    	
    				S[i].append(A[k])
    				k+=1
    			else: break
    		for i in range(N-2,-1,-1):
    			if k<n:
    	
    				S[i].append(A[k])
    				k+=1
    			else: break
    	s=""
    	for i in S:
    		s+="".join(i)
    	return s

s="PAYPALISHIRING"
s="ABCD"
print Solution().convert(s,2)
print "PAHNAPLSIIGYIR"


