from collections import deque

import sys

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if(0<=nx<n and 0<=ny<m):

                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    q.append((nx, ny))

                elif maze[nx][ny] > 1:
                    if (maze[nx][ny] > maze[x][y] + 1):
                        maze[nx][ny] = maze[x][y] + 1

input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())

maze = [list(map(int, input().rstrip('\n'))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

bfs(0, 0)

print(maze[n-1][m-1])