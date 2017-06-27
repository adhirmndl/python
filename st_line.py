class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        n = len(A)
        if (n<=2):
            return n
        elif n>20:print A,B
        m = 0 #result value
        for i in range(n):
            l = {}  #every time reset the dict
            dup = 1 #count the duplicates
            for j in range(n):
                if (A[i]==A[j] and B[i]==B[j] and i!=j):        
                    dup+=1  #count duplicates
                elif i!=j :
                    if (A[i]==A[j]):  #vertical line
                        l['v'] = l.get('v',0) + 1
                    elif (B[i]==B[j]): # horizontal line
                        l['h'] = l.get('h',0) + 1
                    else:   #regular slope
                        slope = 1.0*(B[i]-B[j])/(A[i]-A[j])
                        #print "slope = " , slope , (B[i]-B[j]) , (A[i]-A[j]),i,j
                        l[slope] = l.get(slope,0)+1
            if (len(l)>0): 
                print l.values
                m = max(m,max(l.values())+dup)
            else: #if all points are duplicates, l is empty.
                m = max(m,dup)
        return m

A=  [15, 9, -16, -15, 11, -5, -3, -11, -8, 3, 15, -16, -6, 14, -1, -1, 3, 6, 10, 0, 19, -10, -17, 8, 20, -4, -9, 10, -14, -2, -18, 7, -12, -17, 5, -2, 15, -5, 1, 19, -14, 18, 1, -15, -18, 13, -16, 1, 20, 7, 1, -7, 7, -15, -1, -3, -11, -17, -12, 15, 15, 7, 19, -15, 10, -14, 0, -12, 4, 7, -5, 1, 1, 2, 6, -17, 14, -13, -9, -5, -18, 9, 19, 16, 3, -18, -11, -15, -3, -18, 13, -16, -9, 15, 19, 9]
B= [12, 10, 3, 15, -10, 20, -15, -8, -3, 6, -14, -18, -8, 9, -7, -2, 11, 20, -7, 14, -18, -15, -1, 7, -18, -9, 16, 14, -15, -10, 9, -5, 11, -6, -17, -20, -2, -16, -20, -12, -1, 10, -20, 19, 13, -3, -17, 0, -18, 19, -6, -11, 1, 12, 7, -13, 2, -5, -14, -3, -11, 3, 7, 19, -14, 5, -1, -4, 18, -3, -3, -11, -1, 16, -6, 9, 3, 8, 14, -1, -17, -10, 19, 7, 7, -12, 12, 20, 4, 1, 17, -15, -9, 8, -9, -17]
print Solution().maxPoints(A,B)