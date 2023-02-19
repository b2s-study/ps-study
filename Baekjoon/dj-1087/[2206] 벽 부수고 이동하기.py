import sys
from collections import deque


def is_out_of_range(row, col):
    if (0 <= row < N) and (0 <= col < M):
        return False
    return True


def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] += 1

    while q:
        state, row, col = q.popleft()
        # print(state, row, col)
        if (row == N-1) and (col == M-1):
            return visited[state][row][col]

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if is_out_of_range(nrow, ncol):
                continue

            if (graph[nrow][ncol] == 1) and (state == 0):
                q.append((state + 1, nrow, ncol))
                visited[1][nrow][ncol] = visited[0][row][col] + 1
            elif (graph[nrow][ncol] == 0) and (visited[state][nrow][ncol] == 0):
                q.append((state, nrow, ncol))
                visited[state][nrow][ncol] = visited[state][row][col] + 1
    return -1


input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]

drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]
visited = []
# i=0 -> 벽 부수기 전, i=1 -> 벽 부순 후
for i in range(2):
    visited.append([[0]*M for _ in range(N)])

result = bfs()
print(result)
