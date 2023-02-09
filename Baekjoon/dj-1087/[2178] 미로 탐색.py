import sys
from collections import deque


def bfs(row, col):
    visited[row][col] = True
    q = deque()
    q.append((row, col))

    while (q):
        row, col = q.popleft()

        for i in range(4):
            new_row = row + d_row[i]
            new_col = col + d_col[i]

            if (0 <= new_row < N) and (0 <= new_col < M):
                if visited[new_row][new_col] or (maze[new_row][new_col] == 0):
                    continue
                maze[new_row][new_col] += maze[row][col]
                visited[new_row][new_col] = True
                q.append((new_row, new_col))

    return maze[-1][-1]


input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

d_row = [-1, 0, 0, 1]
d_col = [0, -1, 1, 0]

result = bfs(0, 0)
print(result)

for li in maze:
    print(li)
