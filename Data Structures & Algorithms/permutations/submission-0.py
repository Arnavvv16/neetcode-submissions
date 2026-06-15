class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False]*n
        def sol(subset):
            if len(subset) == n:
               res.append(subset.copy())
               return

            for i in range(0,n):
                if not visited[i]:
                    visited[i] = True 
                    subset.append(nums[i])
                    sol(subset)

                    subset.pop()
                    visited[i]=False

        sol([])
        return res