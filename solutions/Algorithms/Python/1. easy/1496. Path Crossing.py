class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(0, 0)}
        for ch in path:
            if ch == 'N':
                x += 1
            elif ch == 'S':
                x -= 1
            elif ch == 'E':
                y += 1
            elif ch == 'W':
                y -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False
