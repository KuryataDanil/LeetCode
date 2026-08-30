class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
            if left == 0:
                return 0
        return left << shift


print(Solution().rangeBitwiseAnd(1, 2147483647))
