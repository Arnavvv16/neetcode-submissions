# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        cnt = 0
        while curr :
            curr = curr.next 
            cnt +=1
        
        k = cnt - n 
        curr = head 
        if k == 0 :
            curr = curr.next 
            return curr
        curr = head 
        prev = None 

        for i in range(0,k):
            prev = curr
            curr = curr.next
        if curr.next:
            k  = curr.next 
        else :
            k = None
        prev.next = k
        del curr

        return head 

        