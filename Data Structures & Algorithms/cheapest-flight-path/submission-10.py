from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float("inf")] * n
        adj = [[] for _ in range(n)]

        for u, v, p in flights:
            adj[u].append((v, p))

        price[src] = 0

        # [stops, cost, node]
        q = deque()
        q.append((0, 0, src))

        while q:
            stops, currprice, node = q.popleft()

            for desti, money in adj[node]:
                currprice2 = currprice + money

                if currprice2 < price[desti]:
                    stopsnew = stops + 1

                    if stopsnew == k + 1 and desti != dst:
                        continue

                    price[desti] = currprice2
                    q.append((stopsnew, currprice2, desti))

        if price[dst] == float("inf"):
            return -1

        return price[dst]