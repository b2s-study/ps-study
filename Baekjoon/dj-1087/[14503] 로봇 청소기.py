import sys


def next(row, col, direction):
    if direction == NORTH:
        return (row-1, col)
    elif direction == WEST:
        return (row, col-1)
    elif direction == SOUTH:
        return (row+1, col)
    elif direction == EAST:
        return (row, col+1)


def back(row, col, direction):
    if direction == NORTH:
        return next(row, col, direction=SOUTH)
    elif direction == WEST:
        return next(row, col, direction=EAST)
    elif direction == SOUTH:
        return next(row, col, direction=NORTH)
    elif direction == EAST:
        return next(row, col, direction=WEST)


def go(row, col, direction):
    global count
    if not cleaned[row][col]:
        cleaned[row][col] = True
        count += 1

    for _ in range(4):
        direction = TURN[direction]
        nrow, ncol = next(row, col, direction)
        # 벽이거나 이미 청소했는지 확인
        if room[nrow][ncol] == 1 or cleaned[nrow][ncol]:
            continue

        return go(nrow, ncol, direction)

    brow, bcol = back(row, col, direction)
    if room[brow][bcol] == 0:
        return go(brow, bcol, direction)

    return


input = sys.stdin.readline

# d = 0(북), 1(동), 2(남), 3(서) *로봇청소기는 반시계 방향
NORTH, EAST, SOUTH, WEST = 0, 1, 2, 3
TURN = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cleaned = [[False] * M for _ in range(N)]
count = 0
go(r, c, d)

print(count)
