class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 5
        zero = 0
        while x <= n:
            zero += n // x
            x *= 5

        return zero

print(Solution().trailingZeroes(5))