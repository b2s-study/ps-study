import sys


def is_valid(row: int, col: int):
    global rows
    for prev_row in range(row):
        if rows[prev_row] == col:
            return False
        if abs(row - prev_row) == abs(col - rows[prev_row]):
            return False

    return True


def simulate(row: int):
    global rows, count

    if row == N:
        count += 1
        return

    for col in range(N):
        if is_valid(row, col):
            rows[row] = col
            simulate(row + 1)
            rows[row] = -1


input = sys.stdin.readline

N = int(input())
rows = [-1] * N
count = 0
simulate(0)
print(count)
