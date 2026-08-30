class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def f(matr: list[list[any]]) -> None:
            for t in matr:
                print(t)
            print()

        if not grid:
            return 0
        c = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def bfs(i: int, j: int) -> None:
            if visited[i][j]:
                return
            visited[i][j] = True
            if i + 1 < len(grid) and grid[i + 1][j] == '1':
                bfs(i + 1, j)
            if i - 1 >= 0 and grid[i - 1][j] == '1':
                bfs(i - 1, j)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == '1':
                bfs(i, j + 1)
            if j - 1 >= 0 and grid[i][j - 1] == '1':
                bfs(i, j - 1)

        for ii in range(len(grid)):
            for jj in range(len(grid[0])):
                f(visited)
                if grid[ii][jj] == '1' and not visited[ii][jj]:
                    c += 1
                    bfs(ii, jj)
        return c


print(Solution().numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]))
