from collections import Counter
class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        c = Counter()
        n = len(words)
        for word in words:
            c += Counter(word)
        for val in c.values():
            if val % n != 0:
                return False
        return True



print(Solution().makeEqual(["abc","aabc","bc"]))
