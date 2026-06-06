class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashh = {}

        for k in nums :
            hashh[k] = hashh.get(k,0) +1 
        for k,v in hashh.items():
            if v == 1:
                return k