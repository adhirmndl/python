class BST:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
	def insert(self,root,A):
		if not root:
			#print root
			return BST(A)
		if root.val<A:
			root.right = self.insert(root.right,A)
		else:
			root.left = self.insert(root.left,A)
		return root
	def inorder(self,root):
		if not root:return
		self.inorder(root.left)
		print root.val,
		self.inorder(root.right)
	def inorder_iterator(self,A):
		result = []
		Q=[A]
		while len(Q)!=0:
			cur = Q.pop()
			p=[]
			if not cur.left and not cur.right:result.append(cur.val)
			if cur.left:p.append(cur.left)
			if cur.right:p.append(cur.right)
			Q=p+Q
		return result
	def preorder(self,root):
		if not root:return
		print root.val,
		self.inorder(root.left)
		self.inorder(root.right)
	def postorder(self,root):
		if not root:return
		self.inorder(root.left)
		self.inorder(root.right)
		print root.val,
head=None
for i in map(int,raw_input().strip().split()):
	head = Solution().insert(head,i)
print Solution().inorder_iterator(head)
'''print("")
Solution().preorder(head)
print("")
Solution().postorder(head)
print("")'''
