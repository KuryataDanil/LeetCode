class Solution:
    def solve(self, board: list[list[str]]) -> None:
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def bfs(i: int, j: int) -> None:
            if visited[i][j]:
                return
            visited[i][j] = True
            if i + 1 < len(board) and board[i + 1][j] == 'O':
                bfs(i + 1, j)
            if i - 1 >= 0 and board[i - 1][j] == 'O':
                bfs(i - 1, j)
            if j + 1 < len(board[0]) and board[i][j + 1] == 'O':
                bfs(i, j + 1)
            if j - 1 >= 0 and board[i][j - 1] == 'O':
                bfs(i, j - 1)
        for ii in range(len(board)):
            if board[ii][0] == "O":
                bfs(ii, 0)
            if board[ii][len(board[0]) - 1] == "O":
                bfs(ii, len(board[0]) - 1)
        for jj in range(len(board[0])):
            if board[0][jj] == "O":
                bfs(0, jj)
            if board[len(board) - 1][jj] == "O":
                bfs(len(board) - 1, jj)
        print(visited)
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if not visited[i][j]:
                    board[i][j] = "X"
        print(board)


print(Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X", "O","X"],["X","O","X","X"]]))