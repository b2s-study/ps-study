from collections import deque
import sys

input = sys .stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q :
        v = q.popleft()
        result_for_bfs.append(v)

        for i in range(1, n+1):
            if visited[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visited[i] = 1

def dfs(v):
    result_for_dfs.append(v)
    visited[v] = 1

    for i in range(1,n+1):
        if visited[i] == 0 and graph[v][i] == 1 :
          dfs(i)

n , m , v = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)

result_for_bfs = []
result_for_dfs = []

for _ in range (m):
    v1 , v2 = map(int,input().split())
    graph[v1][v2] = graph[v2][v1] = 1

dfs(v)
visited = [0] * (n+1)
bfs(v)

print(*result_for_dfs)
print(*result_for_bfs)
