class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0 
        n = len(nums)
        cnt = 0
        hashmap = {0:1}

        for i in range(0, n):
            prefix_sum += nums[i]
            l = prefix_sum - k
            if l in hashmap:
                cnt = cnt + hashmap[l]

            hashmap[prefix_sum] = hashmap.get(prefix_sum,0) +1 
        return cnt