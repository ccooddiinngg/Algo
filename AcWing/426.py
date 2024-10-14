# https://www.acwing.com/problem/content/428/

"""
1000 5
800 2
400 5
300 5
400 3
200 2
"""

V, N = map(int, input().split())
weights = [0] * N
values = [0] * N
for i in range(N):
    weights[i], important = map(int, input().split())
    values[i] = weights[i] * important

dp = [0] * (V + 1)

for i in range(N):
    for j in range(V, -1, -1):
        if j >= weights[i]:
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

print(dp[V])
