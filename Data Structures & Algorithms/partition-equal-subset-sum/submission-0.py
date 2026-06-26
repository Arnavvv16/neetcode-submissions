class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # dfs
        n = len(nums)
        total = 0
        for k in nums:
            total += k
        if total%2 != 0 :
            return False
        l = total//2
        memo = {}

        def dfs(i,currentsum):
            if currentsum == l :
                return True
            if currentsum>l or i >= n:
                return False

            if (i,currentsum) in memo:
                return memo[(i,currentsum)]
            
            if dfs(i+1, currentsum + nums[i]):
                memo[(i+1, currentsum)] = True
                return True
            if dfs(i+1, currentsum):
                memo[(i+1, currentsum)]= True
                return True

            memo[(i,currentsum)] = False
            return False 

        return dfs(0,0)



