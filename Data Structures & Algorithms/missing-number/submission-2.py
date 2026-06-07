class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k= len(nums)

        for i, num in enumerate(nums):
            k = k^i^num
        return k
        '''for i in range(1,n+1):
            k = k^i
        for num in nums :
            k = k^num
        return k'''

        
