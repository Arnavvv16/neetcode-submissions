# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 2 pointer approach
        curr = head 
        
        l = head
        r = head
        for i in range (0,n):
            r = r.next
        if r == None:
            head = head.next
            return head
        while r.next :
            l = l.next
            r = r.next
        l.next = l.next.next
        return head
        
