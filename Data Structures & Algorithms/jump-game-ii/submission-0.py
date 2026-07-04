class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        lol = [float('inf')] * n
        lol[0] = 0
        for i in range(n):
            k = i 
            for _ in range(nums[i]):
                if k+1<n :
                    lol[k+1] = min(lol[k+1], lol[i] + 1)
                    k+=1
        return lol[n-1]
            
