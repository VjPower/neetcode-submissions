# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2 
        
        if not l2:
            return  l1

        if not l1 and not l2:
            return None 

        head = None 

        if head == None:
            if l1.val > l2.val:
                head = l2
                l2 = l2.next
            else:
                head = l1
                l1 = l1.next 

            ptr = head 

        while l1 and l2:
            if l1.val > l2.val:
                ptr.next = l2
                l2 = l2.next 
            else:
                ptr.next = l1
                l1 = l1.next 
            ptr = ptr.next

        if l1:
            ptr.next = l1
        
        if l2:
            ptr.next = l2 

        return head 
            
        