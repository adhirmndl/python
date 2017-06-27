class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def display(a):
    while a:
        print a.val,
        a=a.next
def insert(head,val):
	if not head : return ListNode(val)
	p=head
	while head.next:
		head=head.next
	head.next=ListNode(val)
	return p
class Solution(self,A):
	def getIntersectionNode(self, A, B):
		pass




a=ListNode(0)
insert(a,1)
insert(a,2)
insert(a,3)
insert(a,4)
insert(a,5)
insert(a,6)
insert(a,7)
display(a)