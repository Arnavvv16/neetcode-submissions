class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*(n+1)
        for i in range(1,n+1):
            if i ==1:
                arr[i] = 1
            elif i == 2:
                arr[i] =2
            else:
                arr[i] = arr[i-1] + arr[i-2]
            
        return arr[n]
    
#o(n) time and o(n) space