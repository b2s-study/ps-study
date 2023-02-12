import sys
from collections import deque
input = sys.stdin.readline

def bfs(x , y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    temp = 1
    global result

    while q :
        point = q.popleft()
        x = point[0]
        y = point[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0 <= ny < n :
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    temp = temp + 1

    results.append(temp)


n = int(input())
graph = []
visited = [[0] * n for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
count = 0
results = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

for i in range (n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j)
            count = count +1


print(count)
results.sort()
for result in results:
    print(result)

