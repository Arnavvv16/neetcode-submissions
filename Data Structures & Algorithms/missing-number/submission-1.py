class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k = 0
        n= len(nums)
        for i in range(1,n+1):
            k = k^i
        for num in nums :
            k = k^num
        return k

