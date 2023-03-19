import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    dist = [-1] * (MAX + 1)
    dist[n] = 0
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(dist[x])
            break

        for nx in (x-1, x+1, x*2):
            if (0<=nx<=MAX) and dist[nx] == -1:
                if (nx == x*2):
                    dist[nx] = dist[x]   # 0초 갱신
                    q.appendleft(nx)     # 순간이동이라 먼저 탐색해야 한다,,,?

                else:   
                    dist[nx] = dist[x] + 1
                    q.append(nx)


MAX = 100000
n, k = map(int, input().rstrip('\n').split())


bfs()