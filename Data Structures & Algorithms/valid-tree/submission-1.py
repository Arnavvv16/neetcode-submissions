class Solution:
    def dfs(self, currnode, prev , visited, adj):
        visited[currnode]=1
        for k in adj[currnode]:
            if visited[k] ==0:
                l = self.dfs(k, currnode, visited,adj)
                if l == False:
                    return False
            elif visited[k] == 1 and k != prev :
                return False
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = [0]*n  # 0 based graph
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        k = self.dfs(0, -1, visited, adj)
        if k == False:
            return False
        return sum(visited) == n
        