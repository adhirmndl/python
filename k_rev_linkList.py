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
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverse(self, A, k):
        a=[]
        while A:
            a.append(A.val)
            A=A.next
        b=[]
        while len(a)>0:
            b+=a[:k][::-1]
            del a[:k]
        p=ListNode(0)
        k=p
        for i in b:
            p.next = ListNode(i)
            p=p.next
        return k.next
        

a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
a.next.next.next=ListNode(4)
a.next.next.next.next=ListNode(5)
a.next.next.next.next.next=ListNode(6)
a.next.next.next.next.next.next=ListNode(7)
a.next.next.next.next.next.next.next=ListNode(8)
a.next.next.next.next.next.next.next.next=ListNode(9)
display(a);print ""
display ( Solution().reverse(a,2))