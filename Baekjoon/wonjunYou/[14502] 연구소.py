from itertools import combinations as c
from collections import deque

import sys
import copy

input = sys.stdin.readline

def bfs(virus):
    virus_pos = deque(virus)
    while virus_pos:
        x, y = virus_pos.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<m):
                if test_lab[nx][ny] == 0:
                    test_lab[nx][ny] = 2
                    virus_pos.append((nx, ny))

n, m = map(int, input().rstrip('\n').split())

lab = []
blank_pos = []

virus = []

for row in range(n):
    lab.append(list(map(int, input().rstrip('\n').split())))
    for col in range(m):
        if lab[row][col] == 2:
            virus.append((row, col))

        if lab[row][col] == 0:
            blank_pos.append((row, col))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
for wall in c(blank_pos, 3):
    test_lab = copy.deepcopy(lab)

    for x, y in wall:
        test_lab[x][y] = 1

    bfs(virus)

    for row in range(n):
        for col in range(m):
            if test_lab[row][col] == 0:
                cnt += 1

    result = max(result, cnt)

print(result)