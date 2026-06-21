class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = [[] for _ in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        result = []
        for u,v in prerequisites:
            adjlist[v].append(u)
            indegrees[u] +=1
        queue = deque()

        for i in range(0, numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for k in adjlist[curr]:
                indegrees[k] -= 1
                if indegrees[k] == 0:
                    queue.append(k)

        return len(result) ==  numCourses
            
            