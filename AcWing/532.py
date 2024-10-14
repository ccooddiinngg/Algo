# https://www.acwing.com/problem/content/534/

"""
2 
4 
3 19 10 6 
5 
11 29 13 19 17 
"""

T = int(input())

for t in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    coins.sort()
    dp = [0] * (coins[-1] + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coins[-1] + 1):
            if j >= coin:
                dp[j] += dp[j - coin]

    res = 0
    for coin in coins:
        if dp[coin] == 1:
            res += 1
    print(res)
