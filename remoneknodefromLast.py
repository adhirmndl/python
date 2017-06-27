# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def Remove(self, A,B):
        n=0
        p=A
        while p:
            n+=1
            p=p.next
        if B>=n:return A.next
        p=A

        for i in range(n-B-1):
            p=p.next
        p.next=p.next.next
        return A

        




    def display(self,A):
    	while A:
    		print A.val,
    		A=A.next

        
            
            

a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
a.next.next.next=ListNode(4)
a.next.next.next.next=ListNode(5)
a.next.next.next.next.next=ListNode(6)
a.next.next.next.next.next.next=ListNode(7)
b=ListNode(5)
b.next=ListNode(6)
b.next.next=ListNode(7)
b.next.next.next=ListNode(8)
b.next.next.next.next=ListNode(9)
b.next.next.next.next.next=ListNode(10)
b.next.next.next.next.next.next=ListNode(11)
Solution().display( Solution().Remove(a,7))