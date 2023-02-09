import sys
from collections import deque


def is_out_of_range(floor, row, col):
    if (0 <= row < ROW_LENGTH) and (0 <= col < COL_LENGTH) and (0 <= floor < HEIGHT):
        return False
    return True


def is_ripe(floor, row, col):
    return container[floor][row][col] == 1


def is_empty(floor, row, col):
    return container[floor][row][col] == -1


def bfs():
    d_row = [-1, 0, 0, 1, 0, 0]
    d_col = [0, -1, 1, 0, 0, 0]
    d_floor = [0, 0, 0, 0, -1, 1]

    q = deque()
    for floor in range(HEIGHT):
        for row in range(ROW_LENGTH):
            for col in range(COL_LENGTH):
                if is_ripe(floor, row, col):
                    q.append((floor, row, col))
                    visited[floor][row][col] = True

    while (q):
        floor, row, col = q.popleft()

        for i in range(6):
            new_row = row + d_row[i]
            new_col = col + d_col[i]
            new_floor = floor + d_floor[i]
            if is_out_of_range(new_floor, new_row, new_col):
                continue
            if visited[new_floor][new_row][new_col]:
                continue
            if is_empty(new_floor, new_row, new_col):
                continue

            q.append((new_floor, new_row, new_col))
            visited[new_floor][new_row][new_col] = True
            days[new_floor][new_row][new_col] = days[floor][row][col] + 1

    return days


input = sys.stdin.readline

# M: col_length, N: row_length
COL_LENGTH, ROW_LENGTH, HEIGHT = map(int, input().split())
container = []
for _ in range(HEIGHT):
    box = [list(map(int, input().split())) for _ in range(ROW_LENGTH)]
    container.append(box)

days = [[[0] * COL_LENGTH for _ in range(ROW_LENGTH)] for _ in range(HEIGHT)]
visited = [
    [[False] * COL_LENGTH for _ in range(ROW_LENGTH)] for _ in range(HEIGHT)]

bfs()

min_day = 0
for floor in days:
    for row in floor:
        row_min = max(row)
        min_day = max(min_day, row_min)

all_visited = True
for floor in range(HEIGHT):
    for row in range(ROW_LENGTH):
        for col in range(COL_LENGTH):
            if visited[floor][row][col] or is_empty(floor, row, col):
                continue
            all_visited = False

if all_visited:
    print(min_day)
else:
    print(-1)
