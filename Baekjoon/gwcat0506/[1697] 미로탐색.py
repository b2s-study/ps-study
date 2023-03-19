import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
# 5 17
def bfs():
    q = deque()
    # 5입력
    q.append(n)
    
    while q:
        x = q.popleft()
        if x==k:
            print(visited[x])
            break
        for j in (x-1,x+1,x*2):
            if 0<= j <= max and not visited[j]:
                # 이동한 위치에 현재 이동한 시간 표시
                visited[j] = visited[x]+1
                
                q.append(j)
max = 100000
visited = [0]*(max+1)
bfs()