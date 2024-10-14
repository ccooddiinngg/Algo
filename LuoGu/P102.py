"""
4 1
1 1 2 3
"""

N, tar = map(int, input().split())
nums = list(map(int, input().split()))

map = {}
ans = 0
for num in nums:
    if map.get(num - tar):
        ans += map.get(num - tar)
    if map.get(num + tar):
        ans += map.get(num + tar)
    map[num] = map.get(num, 0) + 1
print(ans)
