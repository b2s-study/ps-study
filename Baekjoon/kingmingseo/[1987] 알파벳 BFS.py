import sys
input = sys.stdin.readline
from collections import deque
data = []
R, C = map(int,input().split())
for _ in range (R):
    data.append(list(input().rstrip()))
isused = [[False for _ in range(C)] for _ in range(R)]
dx = (1,0,-1,0)
dy = (0,-1,0,1)

answer = 0
def BFS(x,y):
    global answer
    arr = set([(x, y, data[x][y])])

    while arr:
        x, y, ans = arr.pop()
        answer = max(len(ans), answer)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and data[nx][ny] not in ans :
                arr.add((nx,ny,ans + data[nx][ny]))




BFS(0,0)
print(answer)