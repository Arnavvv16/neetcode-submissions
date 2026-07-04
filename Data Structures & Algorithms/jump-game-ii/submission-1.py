class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0 
        r = 0
        jumps = 0

        # Loop until our window's right boundary can reach the last index
        while r < n - 1:
            farthest = 0
            # Use a unique variable name (idx) to avoid shadowing
            for idx in range(l, r + 1):
                farthest = max(farthest, idx + nums[idx])
            
            # Move to the next "window" level
            l = r + 1 
            r = farthest 
            jumps += 1

        return jumps