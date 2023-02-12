from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
    count = 0
    q = deque()
    q.append((x, y))

    graph[x][y] = 0
    count += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<n):
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0
                    count += 1

    return count


n = int(input().rstrip('\n'))

graph = []
results = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 입력
for _ in range(n):
    line = list(map(int, input().rstrip('\n')))
    graph.append(line)

# 시작점 탐색
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            results.append(bfs(x, y))

# 출력
results.sort()

print(len(results))
for result in results:
    print(result)