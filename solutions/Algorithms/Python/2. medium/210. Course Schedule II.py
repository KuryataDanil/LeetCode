class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        stack = []
        valid, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in valid:
                return True

            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)

            valid.add(crs)
            stack.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return stack
