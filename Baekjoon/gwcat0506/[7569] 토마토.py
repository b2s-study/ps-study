from collections import deque
import sys

input = sys.stdin.readline
m, n, h = map(int, input().split())

dq = deque([])

# 3차원 좌표 
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

graph = []
# 토마토 입력
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            # 주의 
            if temp[j][k] == 1:
                dq.append([i, j, k])
    graph.append(temp)

def bfs():
    while dq:
        # 토마토 위치의 좌표받기 
        x, y, z = dq.popleft()
        for i in range(6):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                dq.append([nx, ny, nz])
bfs()

cnt = 0
# 전체 다 찾아봤을 때 토마토를 익히지 못 했다면(0이라면) -1 출력하고 종료
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        # 다 익혔으면 최댓값이 정답 
        cnt = max(cnt, max(j))
print(cnt - 1)