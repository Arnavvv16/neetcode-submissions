class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            if cost[i] > gas[i] :
                continue
            if cost[i] <= gas[i]:
                cnt = 0
                k = i 
                tank = gas[i]
                while cnt < n and tank >= cost[k]  :
                    cnt+=1
                    tank = tank - cost[k] + gas[(k+1)%n]
                    k = (k+1)%n
                if cnt == n :
                    return i
        return -1
        





