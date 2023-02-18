from collections import deque
import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**4)

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<m):
                if iceberg[x][y] > 0 and iceberg[nx][ny] == 0 and not visited[nx][ny]:
                    iceberg[x][y] -= 1

                if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

n, m = map(int, input().rstrip('\n').split())

iceberg = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

year = 1
while True:
    search_count = 0
    visited = [[0] * m for _ in range(n)]

    search_time = 0
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                search_time += 1

    if search_time == 0:
        print(0)
        break

    if search_time > 1:
        print(year - 1)
        break

    year += 1