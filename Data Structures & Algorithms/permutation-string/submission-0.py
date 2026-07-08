class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        
        # Frequency counts for s1 and the first window of s2
        s1_map = {}
        s2_map = {}
        
        for i in range(n):
            s1_map[s1[i]] = s1_map.get(s1[i], 0) + 1
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
            
        # If the first window matches, we are done
        if s1_map == s2_map:
            return True
            
        # Sliding Window
        j = 0 # Left pointer 
        for i in range(n, m): # Right pointer (character entering the window)
            # 1. Add the incoming character to the window
            incoming = s2[i]
            s2_map[incoming] = s2_map.get(incoming, 0) + 1
            
            # 2. Remove or decrement the outgoing character from the window
            outgoing = s2[j]
            if s2_map[outgoing] == 1:
                del s2_map[outgoing] # Remove key entirely if count drops to 0
            else:
                s2_map[outgoing] -= 1
            
            j += 1 # Move left pointer forward
            
            # 3. Check if current window matches s1
            if s1_map == s2_map:
                return True
                
        return False