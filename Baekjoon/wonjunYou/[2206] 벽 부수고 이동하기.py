from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y, check):
    q = deque()
    q.append((x, y, check))

    while q:
        x, y, check = q.popleft()

        if (x == n - 1 and y == m - 1):
            return visited[x][y][check]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<m):
                if board[nx][ny] == 1 and check == 0:
                    visited[nx][ny][1] = visited[x][y][check] + 1
                    q.append((nx, ny, 1))

                elif board[nx][ny] == 0 and visited[nx][ny][check] == 0:
                    visited[nx][ny][check] = visited[x][y][check] + 1
                    q.append((nx, ny, check))

    return -1

n, m = map(int, input().rstrip('\n').split())
board = [list(map(int, input().rstrip('\n'))) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited[0][0][0] = 1

print(bfs(0, 0, 0))