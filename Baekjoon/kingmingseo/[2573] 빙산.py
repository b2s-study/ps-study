import sys
from collections import deque
input = sys.stdin.readline
def BFS(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 :
                    count[x][y] = count[x][y] + 1

                elif graph[nx][ny] != 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    return 1

N , M = map(int,input().split())

graph = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]
answer = 0

button = False

for _ in range(N):
    graph.append(list(map(int,input().split())))

while True:
    result = 0
    visited = [[0] * M for _ in range(N)]
    count = [[0] * M for _ in range(N)]

    for i in range (N):
        for j in range (M):
            if graph[i][j] != 0 and visited[i][j] == 0:
                result = result + BFS(i,j)

    for i in range (N):
        for j in range (M):
            graph[i][j] = graph[i][j] - count[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if result == 0:
        break
    elif result >= 2 :
        button = True
        break

    answer = answer + 1

if button:
    print(answer)
else:
    print(0)

