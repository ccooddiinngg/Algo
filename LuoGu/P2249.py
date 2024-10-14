"""
11 3
1 3 3 3 5 7 9 11 13 15 15
1 3 6
"""

N, Q = map(int, input().split())

nums = list(map(int, input().split()))
query = list(map(int, input().split()))


def find(tar):
    i = 0
    j = N - 1
    while i < j:
        mid = (i + j) // 2
        if nums[mid] >= tar:
            j = mid
        else:
            i = mid + 1
    return i + 1 if nums[i] == tar else -1


for q in query:
    print(find(q), end=" ")
