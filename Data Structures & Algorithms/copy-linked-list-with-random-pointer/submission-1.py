class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. First pass: successfully copy the next pointers (your logic)
        dummy = Node(head.val)
        tail = dummy 

        curr = head.next
        while curr:
            k = Node(curr.val)
            tail.next  = k
            curr = curr.next 
            tail = tail.next

        # 2. Second pass: find the random nodes by calculating their index positions
        curr1 = head 
        curr2 = dummy
        
        while curr1:
            if curr1.random:
                # Calculate the exact index of the random node in the original list
                # by counting steps from the head
                target_index = 0
                temp = head
                while temp != curr1.random:
                    target_index += 1
                    temp = temp.next
                
                # Reset 'a' to the beginning of the cloned list
                a = dummy
                # Walk 'a' forward by that exact number of index steps
                for i in range(target_index):
                    a = a.next 
                curr2.random = a 
            else: 
                curr2.random = None
            
            # CRITICAL FIX: These must happen out here so you don't infinite loop when random is None
            curr1 = curr1.next
            curr2 = curr2.next
            
        return dummy