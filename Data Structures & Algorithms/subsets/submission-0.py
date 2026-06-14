class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def sol(ind, subset):
            if ind >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[ind])
            sol(ind+1, subset)
            subset.pop()
            sol(ind+1,subset)
        sol(0,[])
        return res    