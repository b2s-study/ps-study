from collections import deque

m, n = map(int, input().split())

dq = deque([])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

graph = []

# 토마토 입력
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            dq.append([i, j])

def bfs():
    while dq:
        # 토마토 위치의 좌표받기 
        x, y = dq.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                dq.append([nx, ny])
bfs()

cnt = 0
# 전체 다 찾아봤을 때 토마토를 익히지 못 했다면(0이라면) -1 출력하고 종료
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    # 다 익혔으면 최댓값이 정답 
    cnt = max(cnt, max(i))
print(cnt - 1)