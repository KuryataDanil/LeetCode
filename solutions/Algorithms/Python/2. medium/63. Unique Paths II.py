def uniquePathsWithObstacles(obstacleGrid: list[list[int]]) -> int:
    #print(obstacleGrid)
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = -1
    for i in range(m):
        if obstacleGrid[i][0] == -1:
            break
        obstacleGrid[i][0] = 1
        
    for i in range(n):
        if obstacleGrid[0][i] == -1:
            break
        obstacleGrid[0][i] = 1
           

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == -1:
                continue
            if obstacleGrid[i - 1][j] > 0:
                obstacleGrid[i][j] += obstacleGrid[i - 1][j]
            if obstacleGrid[i][j - 1] > 0:
                obstacleGrid[i][j] += obstacleGrid[i][j - 1]

    return obstacleGrid[-1][-1] if obstacleGrid[-1][-1] > 0 else 0


print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))

# 2