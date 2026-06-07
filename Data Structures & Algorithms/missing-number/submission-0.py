class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
        total = n*(n+1)//2
        for num in nums:
            summ += num
        return (total - summ)
