class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m) ]
    
        def lol (up,do):
            if up== 0 and do == 0 :
                return 1
            if dp[up][do] != -1:
                return dp[up][do]
            elif up>0 and do >0:
                r = lol(up-1, do)
                l = lol(up,do-1)
                dp[up][do] = l+r
                return l+r
            elif up==0:
                l = lol(up, do-1)
                dp[up][do] = l
                return l
            elif do == 0:
                r = lol(up-1,do)
                dp[up][do] =r
                return r
            
        return lol(m-1,n-1)

        #recursion with memoization 