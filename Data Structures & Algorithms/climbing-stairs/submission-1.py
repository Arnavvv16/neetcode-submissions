class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def lol(n):
            if n in memo:
                return memo[n]
            if n ==1 :
                return 1
            if n ==2 :
                return 2
            memo[n] = lol(n-1) + lol(n-2)
            return memo[n]
        
        return lol(n)