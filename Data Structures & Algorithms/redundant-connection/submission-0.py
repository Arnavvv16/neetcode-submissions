class disjoint:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, u,v ):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv :
            return False 
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        elif self.rank[pv] < self.rank[pu]:
            self.parent[pv] = pu
        else:
            self.parent[pu] = pv
            self.rank[pv] +=1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = disjoint(n)

        for u,v in edges :
            if dsu.union(u,v) is False:
                return [u,v]













        