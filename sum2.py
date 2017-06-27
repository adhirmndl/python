class Solution:
	def twoSum(self,A,B):
		d=dict()
		for i in range(len(A)):
			if (A[i]) in d:
				return [d[A[i]]+1,i+1]
			elif B-A[i] not in d:
				d[B-A[i]]=i
		return []



		'''from collections import defaultdict
		d=defaultdict(int)
		print A
		for i in range(len(A)):
			d[B-A[i]]=i+1
		for i in d:
			print d[i],
		print ""
		az=[]		
		for i in range(len(A)):
			if d[A[i]]!=0 and i+1<d[A[i]]:
				az.append([i+1,d[A[i]]])
				#print az
        #print az
        if len(a)==0:return []
		if len(a)==1:return a[0]
		a.sort(key=lambda x: x[1])
		b=[]
		for i in a:
			if i[1]==a[0][1]:
				b.append(i)
			else:break;
		if len(b)==1:
			return b[0]
		b.sort(key=lambda x: x[0])
		return b[0]
		'''
				

a=[5,2,17,11,15,7,4]
a= [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
print Solution().twoSum(a,-3)

