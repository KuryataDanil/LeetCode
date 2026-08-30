class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)
        elif n < 0:
            return self.myPow(1 / x, -n)
        else:
            return x * self.myPow(x * x, n // 2)


print(Solution().myPow(2.10000, 3))
print(Solution().myPow(2.00000, -2))
