class Solution:
	def mul(self,A):
		k=1
		for i in A:
			k*=int(i)
		return k
	def colorful(self,A):
		from collections import defaultdict
		d=defaultdict(bool)
		A=str(A)
		a=[]
		for i in range(1,len(A)+1):
			for j in range(len(A)-i+1):
				a.append( A[j:j+i])
		print a
		for i in a:
			c=self.mul(i)
			if d[c]:return 0
			else:d[c]=True
		return 1
a=12
a=3245
print Solution().colorful(a)


