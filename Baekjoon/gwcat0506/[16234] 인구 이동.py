import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    dq = deque()
    people, count = 0, 0
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        dq.append((x, y))
        count += 1
        people += graph[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    diff = abs(graph[x][y] - graph[nx][ny])
                    if l <= diff <= r:
                        visited[nx][ny] = count
                        q.append((nx, ny))
    while dq:
        x, y = dq.popleft()
        graph[x][y] = (people // count)
    # 국경선을 공유한 지역이 있는지 
    if count == 1:
        return 0
    return 1

answer = 0
while True:
    q = deque()
    break_cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                q.append((i, j))
                break_cnt += bfs(i, j)
    if break_cnt == 0:
        break
    else:
        answer += 1

print(answer)