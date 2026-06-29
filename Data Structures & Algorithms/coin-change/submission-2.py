class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Dictionary to store the minimum coins needed for each amount
        memo = {}
        
        def dfs(rem):
            # Base cases
            if rem == 0:
                return 0
            if rem < 0:
                return -1
            if rem in memo:
                return memo[rem]
            
            min_coins = float('inf')
            
            # Try every coin denomination
            for coin in coins:
                res = dfs(rem - coin)
                
                # If a valid combination was found, update the minimum
                if res != -1:
                    min_coins = min(min_coins, 1 + res)
            
            # Cache the result in memo dictionary
            memo[rem] = min_coins if min_coins != float('inf') else -1
            return memo[rem]
        
        return dfs(amount)