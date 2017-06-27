a=[1,2,3,4,5,6,7,8,69,8,4,21,2,45,4,45,5,45,4,4,455,5,55,55,5,4,11,1,22,2,5,45,45]
a=[1,2,3,4,5,6,7,8,9]
a=[3,5,4,2]
#a=[3, 2, 1]
a=[1,10]
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, a):
        mx=0
        for i in range(len(a)):
        	for j in range(len(a)-1,len(a)-mx-2,-1):
        		print "j = ",j
        		if a[i]<=a[j]:
        			mx=abs(j-i)
        			break
        return mx
print Solution().maximumGap(a)