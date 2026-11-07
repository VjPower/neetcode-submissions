# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0

        count = head

        while count:
            count= count.next 
            length +=1 

        tail = head 

        for _ in range((length+1)//2 - 1):
            tail = tail.next 

        
        mid = tail.next 
        tail.next = None 

        prev = None 
        current = mid 

        while current:
            next = current.next 
            current.next = prev 
            prev = current 
            current = next 

        head1 = head
        while prev:
            prev_next = prev.next 
            head1_next = head1.next 

            head1.next = prev 
            prev.next = head1_next 

            head1 = head1_next 
            prev = prev_next 
