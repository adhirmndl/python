class Solution:
    def prettyJSON(self,A):
    	s=""
    	k=0
    	for i in A:
    		if i in ['{','[','(']:
    			#s+='\n'
    			s+='\t'*k
    			k+=1
    			s+=i
    			#s+=i+'\n' 
    			s+='\t'*k
    		elif i==',':
    			s+=','
    			#s+=',\n'
    			s+='\t'*k
    		elif i in ['}',')',']']:
    			k-=1
    			#s+='\n'
    			s+='\t'*k
    			#s+=i+'\n'
    			s+=i
    		else:s+=i
    	return s



s='{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}'
s='{"id":100,"firstName":"Jack","lastName":"Jones","age":12}'
print Solution().prettyJSON(s)
