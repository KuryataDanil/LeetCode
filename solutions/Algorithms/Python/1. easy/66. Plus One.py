class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        while i != -1:
            digits[i] += 1
            if digits[i] > 10:
                digits[i] = (digits[i] - 1) % 10
            elif digits[i] == 10:
                digits[i] = 0
            else:
                break
            i -= 1
        return digits if i != -1 else [1] + digits


print(Solution().plusOne([9]))
print(Solution().plusOne([1, 2, 3]))

