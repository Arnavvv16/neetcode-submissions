# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        normal = head 
        slow = head 
        fast = head 
        
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next 
        prev = None
        curr = slow.next 
        slow.next=None
        while curr :
            suff = curr.next
            curr.next = prev
            prev = curr 
            curr  = suff

        #prev and head are the heads
        curr1 = head
        curr2 = prev
        while curr2 :
            k1 = curr1.next
            k2 = curr2.next
            curr1.next = curr2
            curr2.next = k1
            curr1 = k1
            curr2 = k2 
        






