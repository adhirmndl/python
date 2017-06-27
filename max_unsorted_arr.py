from itertools import imap, tee
import operator
class Solution:

	def subUnsort(self,A):
		a=[i for i in A]
		a.sort()
		x=[-1,-1]
		for i in range(len(a)):
			if a[i]!=A[i]:
				x[0]=i
				break
		a=a[::-1]
		A=A[::-1]
		for i in range(len(a)):
			print a[i],A[i]
			if a[i]!=A[i]:
				x[1]=len(a)-i-1
				break
		if x[0]==-1:return [-1]
		else:return x








'''
0 10
0	9
1	10
0	8
1	9
2	10


'''


#print Solution().subUnsort([1,4,3,4,5,6,7,11,9])
print Solution().subUnsort([1, 2, 3])
#print Solution().subUnsort([ 1, 1, 10, 10, 15, 10, 15, 10, 10, 15, 10, 15 ])