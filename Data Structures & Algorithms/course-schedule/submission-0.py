class Solution:
    def dfs(self, currnode, visited, pathvisited, adjlist):
        visited[currnode] = 1
        pathvisited[currnode] = 1

        for l in adjlist[currnode]:
            if visited[l] == 0:
                r = self.dfs(l,visited,pathvisited,adjlist)
                if r == True:
                    return True
            elif visited[l] == 1 and pathvisited[l] ==1 :
                return True 
        pathvisited[currnode] = 0
        return False
                

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adjlist[v].append(u)

        visited = [0]*numCourses
        pathvisited = [0]*numCourses

        for i in range(0,numCourses):
            if visited[i] == 0:
                k = self.dfs(i,visited, pathvisited,adjlist)
                if k == True:
                    return False
        return True