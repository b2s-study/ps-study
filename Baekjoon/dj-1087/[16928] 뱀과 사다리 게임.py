import sys
from collections import deque


def bfs(i):
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        cur = q.popleft()
        for i in range(1, 7):
            next = cur + i
            if next > 100:
                continue
            if board[next]:
                next = board[next]
            if visited[next]:
                continue
            visited[next] = True
            state[next] = state[cur] + 1
            q.append(next)

    return state[100]


input = sys.stdin.readline

N, M = map(int, input().split())

board = [0] * 101
for _ in range(N):
    x, y = map(int, input().split())
    board[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    board[u] = v

dice = [i for i in range(1, 7)]
visited = [True] + [False] * 100
state = [0] * 101
print(bfs(1))
