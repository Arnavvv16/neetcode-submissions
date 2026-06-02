class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashh = {}
        n = len(nums)
        for num in nums:
            hashh[num] = hashh.get(num,0)+1
        
        freq = [ [] for i in range(0, n+1)]

        for a,b in hashh.items():
            freq[b].append(a)

        result =[]

        for i in range( n , 0 ,-1 ):
            for a in freq[i]:
                result.append(a)
                if len(result) == k :
                    return result