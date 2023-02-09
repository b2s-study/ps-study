import sys
from collections import deque


def is_out_of_range(row, col):
    if (0 <= row < N) and (0 <= col < N):
        return False
    return True


def bfs(row, col):
    q = deque()
    country_set = set()

    q.append((row, col))
    country_set.add((row, col))

    visited[row][col] = True
    total_people = copied_world[row][col]
    while (q):
        row, col = q.popleft()

        for i in range(4):
            next_row = row + d_row[i]
            next_col = col + d_col[i]

            if is_out_of_range(next_row, next_col) or visited[next_row][next_col]:
                continue

            difference = abs(copied_world[next_row]
                             [next_col] - copied_world[row][col])

            if L <= difference <= R:
                q.append((next_row, next_col))
                country_set.add((next_row, next_col))

                visited[next_row][next_col] = True
                total_people += copied_world[next_row][next_col]

    people_avg = total_people // len(country_set)
    for row, col in country_set:
        world[row][col] = people_avg
    return len(country_set)


input = sys.stdin.readline

N, L, R = map(int, input().split())
visited = [[False] * N for _ in range(N)]
world = [list(map(int, input().split())) for _ in range(N)]

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
days = 0
stop = True
copied_world = []
for i in range(N):
    copied_world.append(world[i].copy())

while(True):
    for row in range(N):
        for col in range(N):
            if visited[row][col]:
                continue

            country_counts = bfs(row, col)
            if country_counts > 1:
                stop = False

    if stop:
        break

    days += 1
    visited = [[False] * N for _ in range(N)]
    stop = True
    for i in range(N):
        copied_world[i] = world[i].copy()

print(days)
