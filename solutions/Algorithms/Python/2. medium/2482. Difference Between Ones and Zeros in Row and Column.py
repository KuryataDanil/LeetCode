class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        rows = []
        cols = []
        for i in range(len(grid)):
            rows.append([grid[i].count(0), grid[i].count(1)])
        for i in range(len(grid[0])):
            zeros = 0
            ones = 0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    ones += 1
                if grid[j][i] == 0:
                    zeros += 1
            cols.append([zeros, ones])
        diff = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(rows[i][1] + cols[j][1] - rows[i][0] - cols[j][0])
            diff.append(temp)
        return diff
