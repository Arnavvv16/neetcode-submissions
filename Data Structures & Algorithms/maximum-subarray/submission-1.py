class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        maxsum = float("-inf")
        
        for num in nums:
            summ += num
            maxsum = max(maxsum, summ)
            
            # If the running sum becomes negative, reset it to 0 
            # so we start fresh with the next element.
            if summ < 0:
                summ = 0
                
        return maxsum