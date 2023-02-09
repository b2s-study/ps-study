
import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v]=1
    result_for_bfs.append(v)
    
    while q:
        # 현재 노트 
        v = q.popleft()
        for i in range(1, len(graph[v])):
            if graph[v][i] == 1 and visited[i] ==0:
                q.append(i)
                visited[i] = 1
                result_for_bfs.append(i)

def dfs(v):
    visited[v]=1
    result_for_dfs.append(v)
    
    for i in range(1, len(graph[v])):
        if graph[v][i] == 1 and visited[i] ==0:
            visited[i]=1
            dfs(i)
            


n, m, v = map(int,input().rstrip().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

result_for_dfs = []
result_for_bfs = []

for _ in range(m):
    v1, v2 = map(int,input().rstrip().split())
    
    graph[v1][v2] = 1
    graph[v2][v1] = 1
    
dfs(v)
print(*result_for_dfs)
visited = [0]*(n+1)

bfs(v)
print(*result_for_bfs)

