from collections import deque
import sys

input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    time_board[n] = 0
    visited[n] = 0

    while q:
        v = q.popleft()

        for next in (v - 1, v + 1, 2 * v):
            if (0<=next<= 100000) and not visited[next]:
                if (next == 2 * v):
                    time_board[next] = min(time_board[next], time_board[v])
                    q.appendleft(next)
                    visited[next] = 1
                    continue

                time_board[next] = min(time_board[next], time_board[v] + 1)
                q.append(next)
                visited[next] = 1

n, k = map(int, input().rstrip('\n').split())

time_board = [100001] * 100001
visited = [0] * 100001

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(n)

print(time_board[k])