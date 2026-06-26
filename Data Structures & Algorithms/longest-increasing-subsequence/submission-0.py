class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        for i in range(n-1,-1,-1):
            for k in range(i,n):
                if nums[k] > nums[i]:
                    lis[i] = max(lis[i],1+lis[k])
        return max(lis)
        


