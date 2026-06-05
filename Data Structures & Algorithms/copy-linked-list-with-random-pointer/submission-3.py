"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(head.val)
        tail = dummy 

        curr = head.next
        while curr:
            k = Node(curr.val)
            tail.next  = k
            curr = curr.next 
            tail = tail.next

        curr1 = head 
        curr2 = dummy
        
        while curr1 :
            
            if curr1.random :
                target = 0
                temp = head 
                while temp != curr1.random:
                    target +=1
                    temp = temp.next 
                 
                a = dummy 
                for i in range(0, target):
                    a = a.next 
                curr2.random = a 
                
            else : 
                curr2.random = None
            
            curr1 = curr1.next
            curr2 = curr2.next
        return dummy


