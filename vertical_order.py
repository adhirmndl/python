# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
	def verticalOrderTraversal(self, A):
		pass

'''
      6
    /   \
   3     7
  / \     \
 2   5     9'''
head = TreeNode(6)
head.left=TreeNode(3)
head.right=TreeNode(7)
head.left.left = TreeNode(2)
head.left.right = TreeNode(5)
head.right.right = TreeNode(9)
print Solution().verticalOrderTraversal(head)