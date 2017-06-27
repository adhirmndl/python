class Solution:
    # @param A : string
    # @return an integer
    def oppo(self,a):
        if a==')':return '('
        elif a=='}':return '{'
        elif a=='[':return '['
    def isValid(self, s):
        fl=True
        if len(s)%2==1:return 0
        a=[]
        for i in s:        
            if i in ['(','{','[']:
                a.append(i)
                
            else:
                if len(a)==0:
                    return 0
                    
                elif a.pop()==oppo(i):
                    continue
                else:
                    return 0
                    
        if len(a)==0: return 1
        else: return 0


a="((((([{()}[]]]{{{[]}}})))))"
#a="((((([{()}[]]{{{[]}}})))))"

print Solution().isValid(a)