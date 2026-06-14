class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def sol(ind,total, subset):
            if total == target:
                res.append(subset.copy())
                return
            
            # Base Case 2: If total exceeds target or we run out of elements
            if total > target or ind >= len(nums):
                return
            subset.append(nums[ind])
            sol(ind, total+nums[ind],subset)
            subset.pop()
            sol(ind+1, total , subset)
        sol(0,0,[])
        return res