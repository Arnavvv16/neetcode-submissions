class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pair = []
        for i in range(0,n):
            pair.append([position[i], speed[i]])
        
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)