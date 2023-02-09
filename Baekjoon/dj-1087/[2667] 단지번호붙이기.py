import sys


def is_out_of_range(i):
    return (i < 0) or (i >= N)


def dfs(x, y):
    visited[x][y] = True
    count = 1
    for i in range(len(direction_x)):
        new_x = x + direction_x[i]
        new_y = y + direction_y[i]

        if is_out_of_range(new_x) or is_out_of_range(new_y):
            continue
        if visited[new_x][new_y] or (house_map[new_x][new_y] == 0):
            continue

        count += dfs(new_x, new_y)

    return count


input = sys.stdin.readline

N = int(input())
house_map = [list(map(int, list(input().rstrip()))) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
direction_x = [-1, 0, 0, 1]
direction_y = [0, -1, 1, 0]

group_count = 0
each_count = []
for x in range(N):
    for y in range(N):
        if visited[x][y] or (house_map[x][y] == 0):
            continue

        count = dfs(x, y)

        group_count += 1
        each_count.append(count)

print(group_count)
each_count.sort()
for count in each_count:
    print(count)
