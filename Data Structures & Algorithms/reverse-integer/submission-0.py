class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        n = abs(x)
        while n>0 :
            ld = n%10 
            result = result*10 + ld
            n = n//10 

        if x < 0:
            result = -result 

        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result