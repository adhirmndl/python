class Solution:
    def subsetsWithDup(self, A):
        n = 2**len(A)
        subsets = set()
        A = sorted(A)
        for i in xrange(n):
            subset = []
            for j, v in enumerate(A):
                print j,v
                if i & (1 << j):
                    subset.append(v)
            print subset
            subsets.add(tuple(subset))

        return sorted(subsets)

a=[1,2,3,4]
print Solution().subsetsWithDup(a)