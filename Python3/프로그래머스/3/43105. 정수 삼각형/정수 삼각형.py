def solution(triangle):
    dp = [[0 for _ in range(len(triangle))] for _ in range(len(triangle))]
    for i in range(len(triangle)):
        dp[len(triangle) - 1][i] = triangle[len(triangle) - 1][i]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = max(dp[i + 1][j + 1] + triangle[i][j], dp[i + 1][j] + triangle[i][j])
    return dp[0][0]