class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        n = len(s)
        i = 0
        j = n-1

        while i < j:
            if s[i] != s[j]:
                return False
            if s[i] == s[j]:
                i +=1
                j-=1
        return True

            
