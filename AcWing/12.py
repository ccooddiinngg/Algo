# https://www.acwing.com/problem/content/12/

"""
4 5
1 2
2 4
3 4
4 6
"""

N, V = map(int, input().split())
vw = [[0 for _ in range(2)] for _ in range(N)]

for i in range(N):
    vw[i][0], vw[i][1] = map(int, input().split())

dp = [[0 for _ in range(V + 1)] for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    for j in range(V, -1, -1):
        dp[i][j] = dp[i + 1][j]
        if j >= vw[i][0]:
            dp[i][j] = max(dp[i][j], dp[i + 1][j - vw[i][0]] + vw[i][1])

ans = V
for i in range(N):
    if dp[i][ans] == dp[i + 1][ans - vw[i][0]] + vw[i][1]:
        print(i + 1, end=" ")
        ans -= vw[i][0]
