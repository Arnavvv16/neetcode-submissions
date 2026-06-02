class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n-1  
        while l <= h :
            m = (l+h)//2
            if nums[m] == target:
                return m
            elif nums[m] > target :
                h= m -1
            else:
                l = m +1 
        return -1