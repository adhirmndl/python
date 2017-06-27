class Solution:
    def fourSum(self, A, B):
        A.sort()
        a=[]
        for i in range(len(A)-3):
            for j in range(i+1,len(A)-2):
                k=j+1
                l=len(A)-1
                while k<l:
                    if A[i]+A[j]+A[k]+A[l] ==B and [A[i],A[j],A[k],A[l]] not in a:
                        a.append([A[i],A[j],A[k],A[l]])
                    elif A[i]+A[j]+A[k]+A[l] <B:k+=1
                    else:l-=1
        return sorted(a) 



a=[5,2,17,11,15,7,4]
a= [ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
a= [ 9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2 ]
print Solution().fourSum(a,0)