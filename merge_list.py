class Solution:
    def merge(self,A,B):
    	a=b=0;
    	k=[]
    	while a<len(A) and b<len(B):
            if A[a]<B[b]:
                k.append(A[a])
                a+=1
            elif A[a]>B[b]:
                k.append(B[b])
                b+=1
            else:
                k.append(A[a])
                k.append(B[b])
                a+=1;b+=1;
        while a!=len(A):
            k.append(A[a])
            a+=1
        while b!=len(B):
            k.append(B[b])
            b+=1

        return k




a=[1, 2, 3, 3, 4, 5, 6]
b=[3, 3, 5]
print Solution().merge(a,b)
