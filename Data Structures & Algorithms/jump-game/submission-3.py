class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        lol = [False]*n
        lol[0] = True
        for i in range(n):
            if lol[i] == True:
                k = i
                for _ in range(nums[i]):
                    if k+1 < n:
                        lol[k+1] = True
                        k+=1
        return lol[-1]


    



