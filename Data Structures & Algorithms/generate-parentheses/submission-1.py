class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def sol(ind, total, subsetstr):
            if ind >= 2 * n:
                if total == 0:
                    res.append(subsetstr)
                return

            if total > n:
                return

            if total < 0:
                return

            sol(ind + 1, total + 1, subsetstr + "(")
            sol(ind + 1, total - 1, subsetstr + ")")

        sol(0, 0, "")
        return res