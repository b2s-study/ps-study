import sys
from collections import deque
input = sys.stdin.readline

def BFS(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1 :
                    q.append((nx, ny))
                    visited[nx][ny] = 1


test_case = int(input())



for _ in range(test_case):
    temp = 0
    M, N, cabbage = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for _ in range(cabbage):
         y, x  = map(int,input().split())
         graph[x][y] = 1


    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and graph[i][j] == 1:
                BFS(i,j)
                temp = temp +1

    print(temp)

