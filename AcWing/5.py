# https://www.acwing.com/problem/content/5/

"""
4 5
1 2 3
2 4 1
3 4 3
4 5 2
"""

N, V = map(int, input().split())

dp = [0] * (V + 1)
vwq = [[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    vwq[i][0], vwq[i][1], vwq[i][2] = map(int, input().split())


def parse(x):
    b = 1
    nums = []
    while x >= b:
        nums.append(b)
        x -= b
        b *= 2
    if x > 0:
        nums.append(x)
    return nums


print(parse(100))

for i in range(N):
    nums = parse(vwq[i][2])
    for num in nums:
        for j in range(V, -1, -1):
            if j >= num * vwq[i][0]:
                dp[j] = max(dp[j], dp[j - num * vwq[i][0]] + num * vwq[i][1])

print(dp[V])
