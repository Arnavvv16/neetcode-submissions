class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits :
            return []
        dic = { "2" : "abc" , "3" : "def", "4" : "ghi", "5":"jkl", "6" : "mno", "7" : "pqrs", "8": "tuv", "9" : "wxyz"}
        res = []
        def sol(ind, subset):
            if ind >= len(digits):
                res.append("".join(subset))
                return 
            letters = dic[digits[ind]]
            for char in letters:
                subset.append(char)
                sol(ind+1,subset)
                subset.pop()
        sol(0,[])
        return res


        