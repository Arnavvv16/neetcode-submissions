class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D grid with 0s
        dp = [[0 for _ in range(n)] for _ in range(m)]
    
        dp[0][0] = 1
        for up in range(m):
            for do in range(n):
                
                if up == 0 and do == 0:
                    continue
                    
               
                if up > 0:
                    from_above = dp[up-1][do]
                else:
                    from_above = 0
                    
             
                if do > 0:
                    from_left = dp[up][do-1]
                else:
                    from_left = 0
                

                dp[up][do] = from_above + from_left
                
        return dp[m-1][n-1]