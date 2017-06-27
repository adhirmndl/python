class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def braces(self, A):
        stack=[]
        for i in A:
            if i in ['(','+','-','*','/']:
                stack.append(i)
                print stack
            elif i==')':
                if len(stack)==0 and stack[-1]=='(':
                    return 1
                else:
                    while len(stack)>0 and stack[-1]!='(':
                        stack.pop()
                        print ("  -- while pop")
                    stack.pop()
                    print  "   --extra pop"
                    print stack
                    
        return 0

a="(a)+(a+b)"
#a="(a+(a+b))"
#a='(())'
a='((a+b))'

#a="((((([{()}[]]]{{{[]}}})))))"
print Solution().braces(a)
