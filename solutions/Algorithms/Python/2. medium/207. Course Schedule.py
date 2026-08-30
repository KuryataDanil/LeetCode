class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            if adj[node] is None:
                return True

            visited.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            visited.remove(node)
            adj[node] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


