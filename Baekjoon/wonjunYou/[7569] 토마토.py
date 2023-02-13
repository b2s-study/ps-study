from collections import deque
import sys

input = sys.stdin.readline

# 방향 : 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
# 며칠이 지나면 모두 익는가?
# 정수 익은것 : 1 익지 않은것 : 0, 토마토가 들어있지 않은 칸 -1
# 모두 익지 못하면 -1. 저장될 때부터 모든 토마토가 익어있는 상태면 0

def bfs(q):
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nz<h and 0<=nx<n and 0<=ny<m):
                if box[nz][nx][ny] == 0:
                    q.append((nz, nx, ny))
                    box[nz][nx][ny] = box[z][x][y] + 1

                elif box[nz][nx][ny] >= 1:
                    if box[nz][nx][ny] > box[z][x][y] + 1:
                        box[nz][nx][ny] = box[z][x][y] + 1
                        q.append((nz, nx, ny))

m, n, h = map(int, input().rstrip('\n').split())
box = [[] for _ in range(h)]

for k in range(h):
    for i in range(n):
        line = list(map(int, input().rstrip('\n').split()))
        box[k].append(line)

q = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                q.append((k, i, j))

bfs(q)

check_ripe = True
max_time = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 0:
                check_ripe = False
                break

            max_time = max(max_time, box[k][i][j])

if check_ripe:
    print(max_time - 1)

else:
    print(-1)