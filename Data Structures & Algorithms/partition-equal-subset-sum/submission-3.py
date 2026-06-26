class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        # If the total sum is odd, we cannot partition it into two equal subsets
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # dp[j] stores whether a subset sum of j is possible
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always possible
        
        for num in nums:
            # Loop backwards from target down to the current number
            for j in range(target, num - 1, -1):
                
                # Case 1: We can already form the sum 'j' WITHOUT using the current 'num'
                if dp[j] == True:
                    dp[j] = True  # Remains True
                
                # Case 2: We check if the remainder (j - num) was possible to form previously
                elif dp[j - num] == True:
                    dp[j] = True  # Becomes True because we can add 'num' to that subset
                
                # Case 3: Neither condition is met
                else:
                    dp[j] = False
                    
        return dp[target]