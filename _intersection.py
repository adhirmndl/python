# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        a=0
        b=0
        aa=A;bb=B;
        while aa:
            a+=1
            aa=aa.next
        while bb:
            b+=1
            bb=bb.next
        if a>b:
            for i in range(b-a+1):
                A=A.next
        elif b>a:
            for i in range(b-a+1):
                B=B.next
        while A and B:
            if A==B:
                return A
            A=A.next
            B=B.next
        return None
a=ListNode(3)
a.next = ListNode(2);a.next .next = ListNode(3);a.next .next.next = ListNode(4);a.next .next.next.next = ListNode(6);a.next .next.next.next.next = ListNode(5);a.next .next.next.next.next .next = ListNode(6)
b=ListNode(3);b.next = ListNode(2);b.next.next = ListNode(3)
b.next.next = a.next.next.next
#print a.val
print Solution().getIntersectionNode(a,b)