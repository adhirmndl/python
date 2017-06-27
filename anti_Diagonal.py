class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def display(self,a):
		for i in range(a):
			print [ii for ii in range(a)]
	def diagonall(self, a):
		c=[]
		ab=len(a[0])+len(a)-1
		for i in range(len(a[0])):
			l=[]
			aa=0
			for j in range(i,-1,-1):
				l.append(a[aa][j])
				aa+=1
			c.append(l)
		#self.display(3)
		for i in range(1,len(a)):
			l=[]
			cc=i
			for j in range(len(a[0])-1,-1,-1):		
				if cc<len(a) and j<len(a):
					l.append(a[cc][j])
				else:break
				cc+=1
			c.append(l)
		return c
	def diagonal(self,a):
		n=len(a)
		k=[0]*(2*n-1)
		
		for i in range(2*n-1):
			k[i]=[]
		print k
		for i in range(n):
			for j in range(n):
				k[i+j].append(a[i][j])
		return k



print Solution().diagonal([[1,2,3],[4,5,6],[7,8,9]])


'''
1 2 3 4 5 6 7 8 9

1 2 4 3 5 7 6 8 9


1 2 3 4
5 6 7 8
9 4 5 2
2 3 4 1




'''