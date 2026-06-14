class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        bracket = [""] * (2*n)
        def sol(ind, total, bracket, res):
            if ind >= 2*n:
                if total == 0:
                    res.append("".join(bracket))
                return
            if total > n:
                return
            elif total < 0:
                return 
            bracket[ind] = "("
            sol(ind +1, total + 1, bracket, res)
            bracket[ind] = ")"
            sol(ind+1, total -1, bracket, res)
        
        sol(0,0, bracket, res)
        return res
                
