class Solution:
    # @param A : integer
    # @return a list of list of integers
    def next(self,lst):
    	b=[1]
    	for i in range(1,len(lst)):
    		b.append(lst[i-1]+lst[i])
    	b.append(1)
    	return b
    def generate(self, A):
    	if A==0:return []
    	elif A==1:return [[1]]
    	c=[[1]]
    	#self.next([1,17,136,680,2380,6188,12376,19448,24310,24310,19448,12376,6188,2380,680,136,17,1 ] )
    	for i in range(A-1):
    		c=(self.next(c))
    	return c

print Solution().generate(0)
print Solution().generate(1)
print Solution().generate(2)
print Solution().generate(3)
print Solution().generate(4)
print Solution().generate(5)
print Solution().generate(6)
print Solution().generate(7)
print Solution().generate(8)
print Solution().generate(9)
print Solution().generate(10)