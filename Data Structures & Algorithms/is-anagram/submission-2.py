class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m :
            return False 
        hashh = {}
        for k in s:
            hashh[k] = hashh.get(k,0)  + 1 
        for ch in t :
            if ch not in hashh:
                return False 
            else :
                if hashh[ch] == 0 :
                    return False
                else:
                    hashh[ch] -= 1
        return True