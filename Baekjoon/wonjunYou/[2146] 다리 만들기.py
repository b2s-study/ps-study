from collections import deque
import sys

MAX_RESULT = 10000

def numbering(x, y, number):
    q = deque()
    q.append((x, y))

    visited[x][y] = 1
    graph[x][y] = number

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<n):
                if graph[nx][ny] > 0 and not visited[nx][ny]:
                    graph[nx][ny] = number
                    q.append((nx, ny))
                    visited[nx][ny] = 1

def bfs(number):
    q = deque()

    for x in range(n):
        for y in range(n):
            if graph[x][y] == number:
                visited[x][y] = 0
                q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<n):
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                if graph[nx][ny] != 0 and graph[nx][ny] != number:
                    return visited[x][y]

input = sys.stdin.readline

n = int(input().rstrip('\n'))

graph = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

number = 1
for x in range(n):
    for y in range(n):
        if graph[x][y] != 0 and not visited[x][y]:
            numbering(x, y, number)
            number += 1

result = MAX_RESULT
for num in range(1, number):
    visited = [[0] * n for _ in range(n)]
    result = min(result, bfs(num))

print(result)