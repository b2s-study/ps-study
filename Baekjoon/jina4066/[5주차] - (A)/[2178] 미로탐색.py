import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<m):
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]
            
#가로, 세로
n, m = map(int, input().rstrip('\n').split())

graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#입력
for _ in range(n):
    line = list(map(int, input().rstrip('\n')))
    graph.append(line)

#출력
print(bfs(0, 0))
