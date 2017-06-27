# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def display(a):
    while a:
        print a.val,
        a=a.next
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        a=0;b=0
        while A:
            a=10*a+A.val
            A=A.next
        while B:
            b=10*b+B.val
            B=B.next

        a=str(a)[::-1]
        b=str(b)[::-1]
        
        a=int (a) + int(b)
        a=str(a)[::-1]
        p=ListNode(0)
        k=p
        for i in a:
            p.next = ListNode(int(i))
            p=p.next
        return k.next



a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
a.next.next.next=ListNode(4)
a.next.next.next.next=ListNode(5)
#a.next.next.next.next.next=ListNode(82)
#a.next.next.next.next.next.next=ListNode(21)
#a.next.next.next.next.next.next.next=ListNode(69)
#a.next.next.next.next.next = a.next.next

display( Solution().addTwoNumbers(a,a))