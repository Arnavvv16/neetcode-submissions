# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 
        curr1 = l1
        curr2 = l2
        carry = 0
        while curr1 or curr2 or carry != 0 :
            if curr1 :
                a = curr1.val
                curr1 = curr1.next
            else:
                a = 0
            if curr2:
                b = curr2.val
                curr2 = curr2.next
            else:
                b = 0
                
            total = a + b + carry 
            carry = total//10

            tail.next = ListNode(total % 10)
            tail = tail.next
        return dummy.next 
