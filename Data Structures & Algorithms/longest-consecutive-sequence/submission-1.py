class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr = set(nums)
        max_count = 0
        for k in arr:
            if k - 1 not in  arr :
                count = 1
                x = k 
                while x+1 in arr:
                    count = count +1
                    x = x +1
                max_count = max(max_count , count)
        
        return max_count
            

