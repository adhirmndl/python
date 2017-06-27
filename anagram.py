class Solution:
    def anagram(self, A):
        from collections import defaultdict
        d=defaultdict(list)
        for i in range(len(A)):
            c= ''.join(sorted(list(A[i])))
            if d[c]:
                d[c].append(i+1)
            else:d[c]=[i+1]
        a=[]
        for i in d:
            a.append(d[i])
        a.sort(key=lambda x: x[0])
        return a



a=[ "cat", "dog", "god", "tca" ]
print Solution().anagram(a)