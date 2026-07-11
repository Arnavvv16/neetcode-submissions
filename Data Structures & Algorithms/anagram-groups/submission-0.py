class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord("a")] += 1
            
            # Convert list to tuple so it's hashable
            key = tuple(cnt) 
            # Initialize the list if the key doesn't exist yet, then append
            if key not in res:
                res[key] = []
            res[key].append(s)
            
        return list(res.values())