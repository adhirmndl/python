class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, b, c):
        l=[]
        for i in A[1:]:
            l.append(str(i))
        A=l
        import itertools
        cnt=0
        for i in itertools.product(A, repeat=b):
            if  int(''.join(i))<c and int(''.join(i))>=(b-1)*10:
                cnt+=1
        return cnt
a=[4,0,1,2,5]
b=2
c=21
a=[0,1,5]
b=1
c=2
print Solution().solve(a,b,c)
