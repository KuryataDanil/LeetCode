class Solution:
    def climbStairs(self, n: int) -> int:
        a_1, a_2 = 1, 2
        if n == 1:
            return a_1
        if n == 2:
            return a_2
        for i in range(2, n):
            a_2, a_1 = a_1 + a_2, a_2,
        return a_2

print(Solution().climbStairs(5))