class Solution:
    def dfs(self, currnode, edges, visited, adjlist):
        visited[currnode] =1 
        for k in adjlist[currnode]:
            if visited[k] == 0 :
                self.dfs(k, edges,visited, adjlist)
        

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [0]*n
        adjlist = [[] for _ in range(n)]
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        cnt = 0
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, edges, visited, adjlist)
                cnt = cnt +1
        return cnt 
