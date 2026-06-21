class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # gotta do bfs
        visited = set()
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque()
        queue.append(("0000",0))
        visited.add("0000")
        while queue:
            curr, lol = queue.popleft()
            if curr == target:
                return lol
            for i in range(0,4):
                digit = int(curr[i])
                for k in [-1,1]:
                    new_digit = str((digit + k) % 10)
                    new = curr[:i] + new_digit + curr[i+1:]
                    if new in visited:
                        continue
                    if new in dead :
                        continue
                    else:
                        visited.add(new)
                        queue.append((new, lol +1))
        return -1 
        


