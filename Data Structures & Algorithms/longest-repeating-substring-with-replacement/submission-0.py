class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        j = 0 
        hashh = {}
        maxf = 0
        res = 0
        for i in range(0,n):
            hashh[s[i]] = hashh.get(s[i], 0) + 1
            maxf = max(maxf, hashh[s[i]])

            while (i-j+1) - maxf > k :
                hashh[s[j]] -=1
                j +=1
            res = max(res, i-j +1)
        return res


