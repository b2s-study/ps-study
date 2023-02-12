import sys
from collections import deque
input = sys.stdin.readline

def BFS(start_point):

    while start_point:
        x, y = start_point.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    start_point.append((nx, ny))
                    visited[nx][ny] = 1
                    graph[nx][ny] = graph[x][y] + 1

M , N = map(int,input().split())
graph = []
visited = [[0] * M for _ in range(N)]
start_point = deque()
answer = -sys.maxsize
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for _ in range(N):
    graph.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 :
            start_point.append((i,j))
            visited[i][j] = 1

BFS(start_point)
button = True
for i in range(N):
    if button == False:
        break

    for j in range(M):
        if graph[i][j] == 0 :
            answer = 0
            button = False
            break

        if graph[i][j] > answer:
            answer = graph[i][j]

print(answer - 1)