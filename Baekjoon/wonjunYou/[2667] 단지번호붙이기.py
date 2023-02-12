import sys

input = sys.stdin.readline

def dfs(x, y):
    global count
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<n and 0<=ny<n):
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                count += 1
                dfs(nx, ny)

    return count

n = int(input().rstrip('\n'))

graph = []
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip('\n'))))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            count = 1
            result.append(dfs(i, j))

result.sort()

print(len(result))

for idx in range(len(result)):
    print(result[idx])