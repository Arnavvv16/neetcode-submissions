class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        queue = deque()
        queue.append((beginWord,1))

        while queue:
            curr, lvl = queue.popleft()
            if curr == endWord:
                return lvl
            
            for i in range(0, len(curr)):
                for c in "abcdefghijklmnopqrstuvwxyz" :
                    if c ==  curr[i] :
                        continue
                    newword = curr[:i] + c + curr[i+1 :]
                    if newword in wordset :
                        queue.append((newword, lvl+1))
                        wordset.remove(newword)
        return 0                   
                    
