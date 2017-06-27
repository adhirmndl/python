import itertools
class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        B_n = len(B[0])
        B=''.join(sorted(B))
        B_N=len(B)
        a=[]
        for i in range(len(A)-len(B)+1):
            s=A[i:i+B_N]
            k=[]
            for ii in range(0,len(s),B_n):
                k.append(s[ii:ii+B_n])
            k.sort()
            k=''.join(k)
            if k==B:a.append(i)
        return a



        '''
        from collections import defaultdict        
        db=defaultdict(int)
        a=[]
        for i in B:
            db[i]+=1
        k=len(''.join(B))
        for i in range(len(A)-len(B[0])+1):
            s=A[i:i+k];flg=True
            print s,i,B
            if len(s)!=k:return a
            for ii in range(0,len(s)-len(B[0])+1,len(B[0])):
                ss=s[ii:ii+len(B[0])]
                print ss
                if s.count(ss)<db[ss]:
                    print db[ss],s.count(ss),ss,s ,"\n   ---> db[ss],s.count(ss),ss,s"
                    flg=False
                    break
            if flg:a.append(i)
        return a'''

b= ['foo','bar']
a= 'barfoothefoobarman'
a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
b = [ "aaa", "aaa", "aaa", "aaa", "aaa" ]
#a= "acaaacbcbccbaabaccabcbbcaaccbbbbcbabaacbbcbccababb"
#b= [ "cabccbbbc", "abbccabbc", "bbbcbbbaa", "acbaabcab", "ccacabccb", "bbacaabca", "acacbaacb", "aabbcccab", "ccccbbcaa", "baaccaabc" ]
#a= "abbaccaaabcabbbccbabbccabbacabcacbbaabbbbbaaabaccaacbccabcbababbbabccabacbbcabbaacaccccbaabcabaabaaaabcaabcacabaa"
#b= [ "cac", "aaa", "aba", "aab", "abc" ]


print Solution().findSubstring(a,b)