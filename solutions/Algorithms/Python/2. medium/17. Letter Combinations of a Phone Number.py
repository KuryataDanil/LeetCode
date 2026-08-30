class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        n = len(digits)
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def backtrack(index: int, temp: str) -> None:
            if index == n:
                res.append(temp)
                return
            for i in range(len(keyboard[digits[index]])):
                backtrack(index + 1, temp + keyboard[digits[index]][i])
        backtrack(0, "")
        return res
