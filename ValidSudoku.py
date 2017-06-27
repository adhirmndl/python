class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def isValidSudoku(self, A):
        #horiziontal test
        print A
        for i in range(len(A)):
            has=[False]*(len(A[0])+1)
            for j in A[i]:
                if j=='.':continue
                elif has[int(j)]:return 01;
                has[int(j)]=True
        for i in range(len(A[0])):
            has = [False]*(len(A)+1)
            for j in A:
                if j[i]=='.':continue;
                elif has[int(j[i])]:return 03;
                has[int(j[i])]=True
        for i in range(0,len(A),3):
            for j in range(0,len(A[0]),3):
                has = [False] * 10
                s=''.join([A[i][j:j+3],A[i+1][j:j+3],A[i+2][j:j+3]])
                for ii in s:
                    if ii=='.':continue
                    if has[int(ii)]:return 0
                    has [int(ii)]=True
        return 1
a= ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
a=[ "....5..1.", ".4.3.....", ".....3..1", "8......2.", "..2.7....", ".15......", ".....2...", ".2.9.....", "..4......" ]
a=  [ "..5.....6", "....14...", ".........", ".....92..", "5....2...", ".......3.", "...54....", "3.....42.", "...27.6.." ]
print Solution().isValidSudoku(a)