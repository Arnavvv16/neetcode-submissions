class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        s = set()
        for i in range(0,n):
            if nums[i] not in s :
                s.add(nums[i])
            else:
                return nums[i]
        
        
