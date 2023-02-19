import sys
from collections import deque


def is_out_of_range(row, col):
    if (0 <= row < R) and (0 <= col < C):
        return False
    return True


def is_goal(row, col):
    if (row == 0) or (row == R-1):
        return True
    elif (col == 0) or (col == C-1):
        return True

    return False


def burn():
    global fires

    new_fires = set()
    for row, col in fires:
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if is_out_of_range(nrow, ncol):
                continue
            if simulation[nrow][ncol] == FIRE:
                continue
            elif simulation[nrow][ncol] == BLOCK:
                continue

            simulation[nrow][ncol] = FIRE
            new_fires.add((nrow, ncol))

    fires = new_fires


def escape(start):
    global time
    q = deque([start])
    row, col = start
    simulation[row][col] = VISITED

    while q:
        row, col = q.popleft()
        if time != times[row][col]:
            burn()
            time = times[row][col]

        if simulation[row][col] == FIRE:
            continue

        # 탈출 성공
        if is_goal(row, col):
            time = times[row][col] + 1
            return True

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if is_out_of_range(nrow, ncol):
                continue
            if simulation[nrow][ncol] != SAFE:
                continue

            q.append((nrow, ncol))
            times[nrow][ncol] = times[row][col] + 1
            simulation[nrow][ncol] = VISITED

    return False


input = sys.stdin.readline

VISITED, SAFE, FIRE, BLOCK = 1, 0, -1, -2
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

R, C = map(int, input().split())
maze = []

fires = set()
simulation = [[0] * C for _ in range(R)]
times = [[0] * C for _ in range(R)]
start = (-1, -1)
for r in range(R):
    row = list(input().rstrip())

    for c in range(C):
        if row[c] == '#':
            simulation[r][c] = BLOCK
        elif row[c] == 'F':
            simulation[r][c] = FIRE
            fires.add((r, c))
        elif row[c] == 'J':
            start = (r, c)

    maze.append(row)

time = 0
possible = escape(start)
if not possible:
    print('IMPOSSIBLE')
else:
    print(time)

# for li in simulation:
#     print(li)
# for li in times:
#     print(li)
