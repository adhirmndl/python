class Solution:
 def fractionToDecimal(self, n, d):
        if n == 0: return "0"
        if d == 0: return ""
        ans = ""
        if(((n < 0)^(d < 0)) > 0): ans = ans + "-"
        n = abs(n)
        d = abs(d)
        ans = ans + str(n/d)
        r = (n%d)*10
        print r,n,d,ans
        if( r == 0): return ans
        dic = {}
        ans = ans + "."
        while r != 0:
            print "r",r
            if r in dic:
                c = dic[r]
                ans = ans[:c] + "(" + ans[c:len(ans)] + ")"
                return ans
            dic[r] = len(ans)
            t = r/d
            ans = ans + str(t)
            r = (r%d) *10
        return ans





#print Solution().fractionToDecimal(20,3)
#print Solution().fractionToDecimal(10,3)
print Solution().fractionToDecimal(22,7)
#print Solution().fractionToDecimal(0,-1)
A = -2147483648
B = -1
print Solution().fractionToDecimal(A,B)
