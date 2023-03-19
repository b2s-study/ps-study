# 아스키 코드를 활용해서 풀어볼 예정
# 065 -> 'A'

import sys
from collections import deque

input = sys.stdin.readline


r,c = map(int,input().split())
strings = [list(map(str,input().rstrip())) for _ in range(r)]

# 아스키 코드로 변환
for i in range(r):
    for j in range(c):
        strings[i][j] = ord(strings[i][j])-65

visited = [0]*26

dx = [-1,1,0,0]
dy = [0,0,-1,1]
maximum = 1

def dfs(x,y,cnt):
    global maximum
    maximum = max(cnt,maximum)
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 방문하지 않았으면 방문
        if 0 <= nx < r and 0 <= ny < c and visited[strings[nx][ny]] == 0:
            visited[strings[nx][ny]] = 1
            dfs(nx,ny,cnt+1)
            visited[strings[nx][ny]] = 0

visited[strings[0][0]] = 1
dfs(0,0,1)
print(maximum)