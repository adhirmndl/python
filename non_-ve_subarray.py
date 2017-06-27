class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self,A):
    	a=[[]]
    	for i in A:
    		if i<0:
    			a.append([])
    		else:
    			a[-1].append(i)
    	
    	mx=0;c=[];fl = True
    	for i in a:
    		if mx<sum(i):
    		    mx=sum(i)
    		    c=i
    		    fl=True
    		elif mx==sum(i):
    			d1=d2=0
    			for i9 in c:
    				d1+=i9
    			for i9 in i:
    				d2+=i9
    			if d2>d1:
    				c=i
    	return c



o=[5,6,4,3,-4,5,4,-6,4,5,6,4]
o=[ -846930886, -1714636915, 424238335, -1649760492 ]
o=[ -1, -1, -1, -1, -1 ]
o=[ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
o=[ 25150, 1412, 82797, 48381, 7065, -47699, -25129, -65483, -64607, -45322, -55176, 27224, 80366, 60444, 70285, -93898, -41133, 96576, -58266, 21711, -20614, -95737, 20591, -48762, -76197, -38588, -54873, 37304, 61200, -68960, 93947 ]
print Solution().maxset(o)