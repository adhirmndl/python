# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A,B):
        if not A: return B
        elif not B:return A
        elif not A and not B:return None
        k=ListNode(0)
        if A.val<B.val:
            k.val=A.val
            k.next= self.mergeTwoLists(A.next,B)
            
        else:
            k.val=B.val;k.next = self.mergeTwoLists(A,B.next)
        return k

        




    def display(self,A):
    	while A:
    		print A.val,
    		A=A.next

        
            
            

a=ListNode(2)
a.next=ListNode(2)
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
Solution().display( Solution().mergeTwoLists(a,b))