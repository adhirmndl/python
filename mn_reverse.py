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
    def reverseBetween(self, A, m, n):
        m-=1;n-=1
        a=[]
        while A:
            a.append(A.val)
            A=A.next
        a=a[:m] + a[m:n+1][::-1] + a[n+1:]
        p=ListNode(0)
        k=p
        for i in a:
            p.next = ListNode(i)
            p=p.next
        return k.next
        

a=ListNode(91)
a.next=ListNode(34)
a.next.next=ListNode(18)
a.next.next.next=ListNode(83)
a.next.next.next.next=ListNode(38)
a.next.next.next.next.next=ListNode(82)
a.next.next.next.next.next.next=ListNode(21)
a.next.next.next.next.next.next.next=ListNode(69)
display(a);print ""
display( Solution().reverseBetween(a,2,4))