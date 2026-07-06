class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(cost) > sum(gas):
            return -1 
        tot = 0
        res = 0

        for i in range(n):
            tot += (gas[i]-cost[i])

            if tot<0 :
                tot = 0
                res = i+1
        return res 

