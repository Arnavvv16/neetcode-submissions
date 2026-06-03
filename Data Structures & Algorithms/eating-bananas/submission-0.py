class Solution:
    def timetaken(self, piles: List[int], speed : int) -> int:
        n = len(piles)
        time = 0
        for i in range(0,n):
            if piles[i]<= speed :
                time = time + 1
            else :
                time = time + (piles[i]+speed - 1 )//speed 
        return time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # o(n)
        ans = r 
        while l <= r:
            m = (l+r)//2
            m_time = self.timetaken(piles,m)

            if m_time <= h :
                ans = m
                r = m -1 
            else:
                l = m +1 
        return ans 
            