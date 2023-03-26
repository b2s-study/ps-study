import sys
from collections import deque


def is_out_of_range(r, c):
    global R, C
    if 0 <= r < R and 0 <= c < C:
        return False
    return True


def bfs(r, c):
    # bfs로 탐색할 수 있는 칸들의 (r,c)와 이전까지 탐색했던 알파벳 list을 q에 담는다.
    global board, max_distance
    q = set()
    q.add((r, c, board[r][c]))

    while q:
        r, c, visited = q.pop()
        max_distance = max(len(visited), max_distance)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if is_out_of_range(nr, nc):
                continue
            if board[nr][nc] not in visited:
                if len(visited) + 1 == R*C or len(visited) == 25:
                    max_distance = len(visited) + 1
                    return
                q.add((nr, nc, visited + board[nr][nc]))


def dfs(r, c):
    # dfs로 0,0 부터 한 칸 한 칸 씩 탐색하며, 탐색한 알파벳을 visited(set)에 넣는다.
    global board, visited, max_distance
    alphabet = board[r][c]
    visited.add(alphabet)

    max_depth = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if is_out_of_range(nr, nc):
            continue

        if board[nr][nc] not in visited:
            max_depth = False
            dfs(nr, nc)

    if max_depth:
        max_distance = max(max_distance, len(visited))
    visited.remove(alphabet)
    # print(len(visited))
    # exit()


input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
visited = set()
max_distance = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# dfs(0, 0)
bfs(0, 0)
print(max_distance)
