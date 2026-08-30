class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        res = money
        min1, min2 = float('inf'), float('inf')
        for price in prices:
            if price <= min2:
                if price <= min1:
                    min1, min2 = price, min1
                else:
                    min2 = price
        #         print(price, min1, min2)
        # print(min1, min2, res)
        return res if res < min2 + min1 else res - (min2 + min1)


print(Solution().buyChoco([1, 2, 2], 3))
print(Solution().buyChoco([69, 91, 78, 19, 40, 13], 94))
