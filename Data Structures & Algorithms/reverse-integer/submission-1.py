class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1
        result = 0
        
        # keep track of sign
        sign = -1 if x < 0 else 1
        n = abs(x)
        
        while n > 0:
            ld = n % 10
            n //= 10
            
            # Check for overflow before multiplying 
            if result > MAX // 10 or (result == MAX // 10 and ld > MAX % 10):
                return 0
                
            result = result * 10 + ld
            
        return result * sign