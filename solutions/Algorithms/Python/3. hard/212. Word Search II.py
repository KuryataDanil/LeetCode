class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()
        rows = len(board)
        cols = len(board[0])
        res = dict()
        for word in words:
            trie.insert(word)

        def dfs(board: list[list[str]], row: int, col: int, path: list[str], node: TrieNode) -> None:
            ch = board[row][col]
            node = node.children.get(ch)
            if node is None:
                return
            path = path + [ch]
            board[row][col] = None
            if node.is_end_of_word:
                res[''.join(path)] = True

            if row + 1 < rows and board[row + 1][col] is not None:
                dfs(board, row + 1, col, path, node)

            if row - 1 >= 0 and board[row - 1][col] is not None:
                dfs(board, row - 1, col, path, node)

            if col + 1 < cols and board[row][col + 1] is not None:
                dfs(board, row, col + 1, path, node)

            if col - 1 >= 0 and board[row][col - 1] is not None:
                dfs(board, row, col - 1, path, node)

            board[row][col] = ch

        for i in range(rows):
            for j in range(cols):
                dfs(board, i, j, [], trie.root)

        return res.keys()
