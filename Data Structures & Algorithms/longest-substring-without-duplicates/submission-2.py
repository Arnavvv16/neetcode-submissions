class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0
        
        # 'r' acts as the right pointer of your sliding window
        for r in range(len(s)):
            # If we find a duplicate, shrink the window from the left
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                
            # Add the current character to the window
            char_set.add(s[r])
            
            # Update the max length found so far
            max_len = max(max_len, r - l + 1)
            
        return max_len