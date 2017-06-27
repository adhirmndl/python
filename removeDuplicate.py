# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        from collections import defaultdict
        d=defaultdict(int)
        while A:
            d[A.val]+=1
            A=A.next
        k=ListNode(0)
        p=k
        for i in d:
        	if d[i] ==1:
        		k.next=ListNode(i)
        		k=k.next
       	return p.next

        #for i in d:
        #	c.next = ListNode(i)
        #	c=c.next
        #return kk.next





    def display(self,A):
    	while A:
    		print A.val,
    		A=A.next

        
            
            

a=ListNode(2)
a.next=ListNode(2)
a.next=ListNode(2)
a.next.next=ListNode(2)
a.next.next.next=ListNode(2)
a.next.next.next.next=ListNode(2)
a.next.next.next.next.next=ListNode(2)
a.next.next.next.next.next.next=ListNode(3)
Solution().display( Solution().deleteDuplicates(a))