# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def partition(self, A,B):
        '''
        n=0
        p=A
        while p:
            n+=1
            p=p.next
        B=B%n
        for i in range(B):
            A=self.rt(A)
        return A
        '''
        n=0
        p=A
        while p:
            n+=1
            p=p.next
        a=[]
        b=[]
        p=A
        n=0
        while p:
            n+=1
            if p.val<B:a.append(p.val)
            else:b.append(p.val)
            p=p.next
        a=a+b
        k=ListNode(0)
        p=k
        for i in a:
            k.next=ListNode(i)
            k=k.next
        
        return p.next



        




    def display(self,A):
    	while A:
    		print A.val,
    		A=A.next

        
            
            

a=ListNode(91)
a.next=ListNode(34)
a.next.next=ListNode(18)
a.next.next.next=ListNode(83)
a.next.next.next.next=ListNode(38)
a.next.next.next.next.next=ListNode(82)
a.next.next.next.next.next.next=ListNode(21)
a.next.next.next.next.next.next.next=ListNode(69)
#91 -> 34 -> 18 -> 83 -> 38 -> 82 -> 21 -> 69


b=ListNode(5)
b.next=ListNode(6)
b.next.next=ListNode(7)
b.next.next.next=ListNode(8)
b.next.next.next.next=ListNode(9)
b.next.next.next.next.next=ListNode(10)
b.next.next.next.next.next.next=ListNode(11)
Solution().display( Solution().partition(a,int(raw_input())))