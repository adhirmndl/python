class Solution:
	def lszero(self,A):
		for i in range(len(A)):
			for j in range(i+1):
				if sum (A[j:j+len(A)-i])==0:
					return A[j:j+len(A)-i]

	def lszero(self, A):
		print A
		from collections import defaultdict
		N = len(A)
		pre = [None]*N
		curr = 0
		for i in xrange(N):
			curr += A[i]
			pre[i] = curr
		print pre

		seen_table = defaultdict(list)
		seen_table[0]=[-1]
		longest = -1
		indices = None
		for i in xrange(N):
			s = pre[i]
			seen_table[s].append(i)

			gap = seen_table[s][-1] - seen_table[s][0]
			print gap,longest
			if gap > longest:
				longest = gap
				indices = (seen_table[s][0]+1,seen_table[s][-1]+1)
				print indices
		if indices:
			return A[indices[0]:indices[1]]
		else:
			return []

a=[1 ,2 ,-2 ,4 ,-4]
#a=['a','b','c','d','e','f','g','h','i','j']
print Solution().lszero(a)