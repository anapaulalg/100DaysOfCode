# Unique Paths

def uniquePaths(m, n):
    dp = [[0]*n for x in range(m)]
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[m-1][n-1]

if __name__ == "__main__":
    m = 7
    n = 3
    print(uniquePaths(m, n))