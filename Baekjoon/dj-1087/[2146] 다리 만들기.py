import sys
from collections import deque


def is_out_of_range(row, col):
    if (0 <= row < N) and (0 <= col < N):
        return False
    return True


def scan(srow, scol, sirial_num):
    q = deque([(srow, scol)])
    visited[srow][scol] = True
    country[srow][scol] = sirial_num

    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if is_out_of_range(nrow, ncol) or visited[nrow][ncol]:
                continue

            if country[nrow][ncol] != SEA:
                q.append((nrow, ncol))
                visited[nrow][ncol] = True
                country[nrow][ncol] = sirial_num
            else:
                boundary.add((row, col))


def is_other_island(row, col, current_island):
    return country[row][col] != SEA and country[row][col] != current_island


def simulate(srow, scol):
    global simulation
    q = deque([(srow, scol)])
    start_island = country[srow][scol]

    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if is_out_of_range(nrow, ncol) or simulation[nrow][ncol] != 0:
                continue
            if country[nrow][ncol] == SEA:
                q.append((nrow, ncol))
                simulation[nrow][ncol] += simulation[row][col] + 1
            if is_other_island(nrow, ncol, start_island):
                return simulation[row][col]

    return -1


input = sys.stdin.readline

N = int(input())
country = [list(map(int, input().split())) for _ in range(N)]

# 1. bfs를 통해 섬을 구별한다.
# 2. 바다=0, 다리=-1, 섬은 각각 번호(예> 1, 2, 3)로 지정한다.
# 3. bfs를 통해 최단 다리 길이를 구한다.

SEA, BRIDGE = 0, -1
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]
visited = [[False] * N for _ in range(N)]

boundary = set()
serial_number = 1
for row in range(N):
    for col in range(N):
        if country[row][col] == 1 and not visited[row][col]:
            scan(row, col, serial_number)
            serial_number += 1

min_distance = 2*N
for row, col in boundary:
    simulation = [[0] * N for _ in range(N)]
    distance = simulate(row, col)
    if distance != -1:
        min_distance = min(min_distance, distance)

print(min_distance)
