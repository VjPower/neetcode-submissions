class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur_l1 = l1 
        cur_l2 = l2 

        current = None 
        carry = 0 

        while cur_l2 and cur_l1:
            sum = (cur_l2.val + cur_l1.val + carry)%10
            carry = (cur_l2.val + cur_l1.val + carry)//10
            if not current:
                current = ListNode(sum)
                head = current
            else:
                current.next = ListNode(sum)
                current = current.next 

            cur_l1 = cur_l1.next 
            cur_l2 = cur_l2.next

        while cur_l2:
            sum = (cur_l2.val + carry)%10 
            carry = (cur_l2.val + carry)//10

            current.next = ListNode(sum)
            current = current.next 

            cur_l2 = cur_l2.next 

        while cur_l1:
            sum = (cur_l1.val + carry)%10 
            carry = (cur_l1.val + carry)//10

            current.next = ListNode(sum)
            current = current.next 
            
            cur_l1 = cur_l1.next

        if carry>0:
            current.next = ListNode(carry)

        return head