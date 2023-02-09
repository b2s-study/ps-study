import sys

sys.setrecursionlimit(10**6)


def is_out_of_range(index, length):
    return (index < 0) or (index >= length)


def dfs(row, col):
    visited[row][col] = True

    for i in range(4):
        new_row = row + row_direction[i]
        new_col = col + col_direction[i]
        if is_out_of_range(new_row, N) or is_out_of_range(new_col, M):
            continue

        if visited[new_row][new_col] or (field[new_row][new_col] == 0):
            continue

        dfs(new_row, new_col)


input = sys.stdin.readline

row_direction = [-1, 0, 0, 1]
col_direction = [0, -1, 1, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    bug_count = 0
    for row in range(N):
        for col in range(M):
            if visited[row][col] or (field[row][col] == 0):
                continue

            dfs(row, col)
            bug_count += 1

    print(bug_count)
