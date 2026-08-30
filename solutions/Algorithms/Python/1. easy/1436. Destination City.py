class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        return str(set([i[1] for i in paths]).difference(set([i[0] for i in paths])))[2:-2]
