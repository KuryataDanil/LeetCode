class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(left: int, right: int, s: str) -> None:
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                backtrack(left + 1, right, s + '(')
            if right < left:
                backtrack(left, right + 1, s + ')')

        backtrack(0, 0, "")
        return res


print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))
