import sys
from collections import deque


def is_out_of_range(row, col):
    if (0 <= row < ROW_LENGTH) and (0 <= col < COL_LENGTH):
        return False
    return True


def is_ripe(row, col):
    return box[row][col] == 1


def is_empty(row, col):
    return box[row][col] == -1


def bfs():
    d_row = [-1, 0, 0, 1]
    d_col = [0, -1, 1, 0]

    q = deque()
    for row in range(ROW_LENGTH):
        for col in range(COL_LENGTH):
            if is_ripe(row, col):
                q.append((row, col))
                visited[row][col] = True

    while (q):
        row, col = q.popleft()

        for i in range(4):
            new_row = row + d_row[i]
            new_col = col + d_col[i]
            if is_out_of_range(new_row, new_col) or visited[new_row][new_col] or is_empty(new_row, new_col):
                continue

            q.append((new_row, new_col))
            visited[new_row][new_col] = True
            days[new_row][new_col] = days[row][col] + 1

    return days


input = sys.stdin.readline

# M: col_length, N: row_length
COL_LENGTH, ROW_LENGTH = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(ROW_LENGTH)]
days = [[0] * COL_LENGTH for _ in range(ROW_LENGTH)]
visited = [[False] * COL_LENGTH for _ in range(ROW_LENGTH)]

bfs()

min_day = 0
for row in days:
    row_min = max(row)
    min_day = max(min_day, row_min)

all_visited = True
for row in range(ROW_LENGTH):
    for col in range(COL_LENGTH):
        if visited[row][col] or is_empty(row, col):
            continue
        all_visited = False

if all_visited:
    print(min_day)
else:
    print(-1)
