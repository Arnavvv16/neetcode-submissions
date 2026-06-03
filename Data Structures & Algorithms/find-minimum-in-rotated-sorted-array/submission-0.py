class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        minn = 1001
        while l <= h:
            m = (l+h)//2
            if nums[l]< nums[m]< nums[l]:
                minn = min(minn, nums[l])
                
            elif nums[m]>= nums[l]:
                minn = min(minn, nums[l])
                l = m +1
            elif nums[m]<= nums[h]:
                minn = min(minn,nums[m])
                h = m - 1
            
        return minn