
class Solution:
    def single(self,A):
    	from collections import defaultdict
    	d=defaultdict(int)
    	s=[]
    	for i in A:
    		d[i]+=1
    		if d[i]==2:
    			s.remove(i)
    		elif d[i]==1:
    			s.append(i)
    	return s[0]