import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**4)

def dfs(x, y):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<n and 0<=ny<m):
            if (field[nx][ny] == 1 and visited[nx][ny] == 0):
                dfs(nx, ny)

T = int(input().rstrip('\n'))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
    m, n, k = map(int, input().rstrip('\n').split())

    field = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().rstrip('\n').split())

        field[y][x] = 1

    result = 0
    for x in range(n):
        for y in range(m):
            if (field[x][y] == 1 and visited[x][y] == 0):
                result += 1
                dfs(x, y)

    print(result)