class Solution:
    def minOperations(self, s: str) -> int:
        counter1 = 0
        counter2 = 0
        i = 0
        for ch in s:
            if i % 2 == 0:
                if ch == '0':
                    counter1 += 1
                else:
                    counter2 += 1
            else:
                if ch == '1':
                    counter1 += 1
                else:
                    counter2 += 1
            i += 1
        return min(counter1, counter2)

