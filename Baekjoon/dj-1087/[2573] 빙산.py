import sys
from collections import deque


def is_out_of_range(row, col):
    if (0 <= row < N) and (0 <= col < M):
        return False
    return True


def bfs(row, col):
    q = deque()
    q.append((row, col))
    checked[row][col] = True

    while(q):
        row, col = q.popleft()

        for i in range(4):
            next_row = row + d_row[i]
            next_col = col + d_col[i]

            if is_out_of_range(next_row, next_col) or checked[next_row][next_col]:
                continue
            if mount[next_row][next_col] == 0:
                if mount[row][col] > 0:
                    mount[row][col] -= 1
            else:
                q.append((next_row, next_col))
                checked[next_row][next_col] = True
    return


input = sys.stdin.readline

N, M = map(int, input().split())
mount = [list(map(int, input().split())) for _ in range(N)]
checked = [[False] * M for _ in range(N)]
d_row = [0, 0, 1, -1]
d_col = [1, -1, 0, 0]

years = 0

while(True):
    mount_count = 0
    for row in range(N):
        for col in range(M):
            if mount[row][col] != 0 and not checked[row][col]:
                bfs(row, col)
                mount_count += 1

    if mount_count == 0:
        years = 0
        break

    years += 1
    if mount_count >= 2:
        years -= 1
        break

    checked = [[False] * M for _ in range(N)]


print(years)
