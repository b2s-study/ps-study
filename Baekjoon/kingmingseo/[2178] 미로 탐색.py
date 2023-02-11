import sys
from collections import deque
input = sys.stdin.readline
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1


    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and  0 <= ny < m :
                if visited[nx][ny] == 0 and maze[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

n , m = map(int,input().split())
maze = []
visited = [[0] * m for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(n):
    maze.append(list(map(int,input().rstrip())))

bfs(0,0)
print(visited[n-1][m-1])