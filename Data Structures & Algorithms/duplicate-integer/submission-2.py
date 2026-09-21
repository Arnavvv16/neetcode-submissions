class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap ={}
        for k in nums:
            hashmap[k] = hashmap.get(k,0) +1 
        for k,v in hashmap.items():
            if v > 1:
                return True 
        return False