import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (2<=nx<=100 and 2<=ny<=100):
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0

    return count
            

#가로, 세로
n, m = map(int, input().rstrip('\n').split())

count = 0
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#입력
for _ in range(n):
    line = list(map(int, input().rstrip('\n')))
    graph.append(line)

#시작점 탐색
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            bfs(x,y)
            count += 1

#출력
print(count)
