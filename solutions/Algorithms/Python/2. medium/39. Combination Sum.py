class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        s = set(candidates)
        res = []

        def backtrack(candidates: list[int], target: int, path: list[int]) -> None:
            if target == 0:
                res.append(path)
            elif target < 0:
                return
            for i in range(len(candidates)):
                backtrack(candidates[i:], target - candidates[i], path + [candidates[i]])

        backtrack(candidates, target, [])

        return res
