class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):        
        if len(A)==0:
            return 0
        from collections import defaultdict
        d=defaultdict(list)
        prs=defaultdict(bool)
        for i in range(len(A)):
            d[A[i]+B].append(i)
            prs[A[i]+B] = True
        for i in range(len(A)):
            
            if prs[A[i]]:
                if len(d[A[i]])>1:return 1
                elif len(d[A[i]])==1 and i!=d[A[i]][0]:return 1
        return 0


a= [ 70, 48, 90 ]
b= 70
print Solution().diffPossible(a,b)