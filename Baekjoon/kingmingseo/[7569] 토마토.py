import sys
from collections import deque
input = sys.stdin.readline

def BFS(start_point):

    while start_point :
        z , x , y = start_point.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < Floor:
                if graph[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                    start_point.append((nz, nx, ny))
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    visited[nz][nx][ny] = 1



M, N , Floor = map(int,input().split())
graph = []
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(Floor)]
start_point = deque()
answer = -sys.maxsize
Button = False
for i in range (Floor):
    temp = []

    for j in range(N):
        temp.append(list(map(int,input().split())))

    graph.append(temp)

for i in range(Floor):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                start_point.append((i, j, k))
                visited[i][j][k] = 1

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

BFS(start_point)

for i in range(Floor):
    if Button == True:
        break
    for j in range(N):
        if Button == True:
            break
        for k in range(M):
            if graph[i][j][k] == 0 :
                Button = True
                answer = 0
                break
            elif graph[i][j][k] > answer :
                answer = graph[i][j][k]

print(answer - 1)

