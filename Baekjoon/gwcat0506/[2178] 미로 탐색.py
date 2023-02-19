
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))      
    return 


t =  int(input())
for _ in range(t):
    cnt = 0
    n,m,K = map(int,input().split())
    
    # 가로세로 주의 !
    graph = [[0]*m for _ in range(n)]
    
    for _ in range(K):
        x,y = map(int,input().split())
        graph[x][y] = 1
        
    
    for a in range(n):
        for b in range(m):
            if graph[a][b]==1:
                bfs(graph,a,b)
                cnt+=1
                
    print(cnt)