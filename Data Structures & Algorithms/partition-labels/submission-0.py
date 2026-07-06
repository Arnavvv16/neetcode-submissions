class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        lol = {}

        for i,c in enumerate(s): # value and index at same tiem\
            lol[c] = i
        
        res = []
        size = 0
        end = 0 

        for i,c in enumerate(s): # traversal
            size +=1
            end = max(end, lol[c])

            if end == i:
                res.append(size)
                size = 0

        return res

        




