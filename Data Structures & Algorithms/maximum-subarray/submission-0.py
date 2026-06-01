class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = float("-inf")
        maxsum = float("-inf")

        for i in range(0, len(nums)):
            if summ < 0:
                summ = 0
                summ = summ + nums[i]
                maxsum = max(maxsum,summ)
            else:
                summ = summ+nums[i]
                maxsum = max(maxsum,summ)
        return maxsum
        