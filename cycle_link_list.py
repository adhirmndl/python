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
    def addTwoNumbers(self, A):
        slow = A;fast = A.next;
        try:            
            while slow!=fast:
                slow=slow.next

                fast=fast.next.next
            return slow

        except:
            return None
        



a=ListNode(1)
a.next=ListNode(2)
a.next.next=ListNode(3)
a.next.next.next=ListNode(4)
a.next.next.next.next=ListNode(5)
#a.next.next.next.next.next=ListNode(82)
#a.next.next.next.next.next.next=ListNode(21)
#a.next.next.next.next.next.next.next=ListNode(69)
a.next.next.next.next.next = a.next.next.next
#display(a)
print ( Solution().addTwoNumbers(a))