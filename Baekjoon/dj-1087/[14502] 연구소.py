import sys
import copy
from collections import deque
from itertools import combinations


def is_out_range_of(row, col):
    if (0 <= row < N) and (0 <= col < M):
        return False
    return True


def bfs(simulation):
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            if not visited[y][x] and (simulation[y][x] == 2):
                q = deque()
                q.append((y, x))
                visited[y][x] = True

                while q:
                    row, col = q.popleft()
                    for i in range(4):
                        nrow = row + drow[i]
                        ncol = col + dcol[i]
                        if is_out_range_of(nrow, ncol):
                            continue
                        if visited[nrow][ncol]:
                            continue

                        if simulation[nrow][ncol] == 0:
                            q.append((nrow, ncol))
                            simulation[nrow][ncol] = 2
                            visited[nrow][ncol] = True
    return


input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 벽을 미리 세워놓고
# 바이러스 퍼뜨린 후
# 남아있는 안전 지역 수 계산
# 가장 많이 남아있는 경우의 안전지역 개수 출력

points = []
for row in range(N):
    for col in range(M):
        if graph[row][col] == 0:
            points.append((row, col))
wall_cases = list(combinations(points, 3))

result = 0
for case in wall_cases:
    simulation = copy.deepcopy(graph)

    for row, col in case:
        simulation[row][col] = 1

    bfs(simulation)

    safe_zones = 0
    for row in simulation:
        safe_zones += row.count(0)
    # if safe_zones > result:
    #     for li in simulation:
    #         print(li)
    result = max(result, safe_zones)

print(result)
