class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        lenWord = len(word)
        res = dict()

        def backtracing(board: list[list[str]], row: int, col: int, path: list[str], index: int) -> None:
            ch = board[row][col]
            if word[index] != ch:
                return
            path = path + [ch]
            board[row][col] = None
            if index == lenWord - 1:
                res[''.join(path)] = True
                return

            if row + 1 < rows and board[row + 1][col] is not None:
                backtracing(board, row + 1, col, path, index + 1)

            if row - 1 >= 0 and board[row - 1][col] is not None:
                backtracing(board, row - 1, col, path, index + 1)

            if col + 1 < cols and board[row][col + 1] is not None:
                backtracing(board, row, col + 1, path, index + 1)

            if col - 1 >= 0 and board[row][col - 1] is not None:
                backtracing(board, row, col - 1, path, index + 1)

            board[row][col] = ch

        for i in range(rows):
            for j in range(cols):
                backtracing(board, i, j, [], 0)

        return res.keys()
