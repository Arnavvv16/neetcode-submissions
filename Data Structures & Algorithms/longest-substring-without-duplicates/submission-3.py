class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not s:
            return 0
        myset = set()
        j = 0
        ans = 0

        for i in range(0,n):
            while s[i] in myset:
                myset.remove(s[j])
                j +=1
            myset.add(s[i])
            ans = max(ans, i-j +1)
        
        return ans


