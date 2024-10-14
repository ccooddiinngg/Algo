"""
*...*.....
......*...
...*...*..
..........
...*.F....
*.....*...
...*......
..C......*
...*.*....
.*.*......
"""


def key(p1, d1, p2, d2):
    return str(p1) + str(d1) + str(p2) + str(d2)


N = 10
g = [list(input()) for _ in range(N)]

pF = [0, 0]
pC = [0, 0]
for i in range(N):
    for j in range(N):
        if g[i][j] == "F":
            pF = [i, j]
        if g[i][j] == "C":
            pC = [i, j]

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dF = 0
dC = 0

visited = set()
ans = 0
circle = False

while pF != pC:
    x = pF[0] + dir[dF][0]
    y = pF[1] + dir[dF][1]
    if x < N and x >= 0 and y < N and y >= 0 and g[x][y] != "*":
        pF[0], pF[1] = x, y
    else:
        dF = (dF + 1) % 4

    x = pC[0] + dir[dC][0]
    y = pC[1] + dir[dC][1]
    if x < N and x >= 0 and y < N and y >= 0 and g[x][y] != "*":
        pC[0], pC[1] = x, y
    else:
        dC = (dC + 1) % 4

    k = key(pF, dF, pC, dC)
    # print(k)
    if k in visited:
        circle = True
        break
    else:
        visited.add(k)

    ans += 1

print(0 if circle else ans)
