class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        count1, count2 = 0, 0
        res = 0

        for i in range(len(bank) - 1):
            if count1 == 0:
                count1 = bank[i].count('1')
            elif count2 != 0:
                count1 = count2
            count2 = bank[i + 1].count('1')

            res += count1 * count2
        return res

