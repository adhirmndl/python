class Solution:
    # @param root : root node of tree
    # @param sum1 : integer
    # @return a list of list of integers
    def path(self,A,B,s,p):
        if not A.left and not A.right and B==s+A.val:
            self.a.append(p + [A.val])
            return
        if A.left:self.path(A.left,B,A.val+s,p+[A.val])
        if A.right:self.path(A.right,B,A.val+s,p+[A.val])
    def pathSum(self, A, sum1):
        self.a = []
        self.path(A,sum1,0,[])
        return self.a
