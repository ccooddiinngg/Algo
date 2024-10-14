"""
4 7
20 15 10 17
"""

n, tar = map(int, input().split())
nums = sorted(list(map(int, input().split())))
sums = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    sums[i] = sums[i + 1] + nums[i]
    if sums[i] - (n - i) * (0 if i == 0 else nums[i - 1]) >= tar:
        print((sums[i] - tar) // (n - i))
        break
