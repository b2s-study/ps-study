from collections import deque
import sys

input = sys.stdin.readline

def fire_spread(q):
    fire_can_go = len(q)

    for _ in range(fire_can_go):
        x, y = q.popleft()
        maze[x][y] = "F"

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<r and 0<=ny<c):
                if maze[nx][ny] == ".":
                    q.append((nx, ny))

    return q

def bfs(q):
    global can_escape
    player_can_go = len(q)

    for _ in range(player_can_go):
        x, y = q.popleft()

        if ((x == 0 or x == r - 1) or (y == 0 or y == c - 1)):
            can_escape = True
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<r and 0<=ny<c):
                if maze[nx][ny] == "." and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    return q

r, c = map(int, input().rstrip('\n').split())

maze = [list(input().rstrip('\n')) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

player_q = deque()
fire_q = deque()

for x in range(r):
    for y in range(c):
        if maze[x][y] == "J":
            player_q.append((x, y))
            visited[x][y] = 1

        if maze[x][y] == "F":
            fire_q.append((x, y))

time = 1
can_escape = False
while True:
    fire_q = fire_spread(fire_q)
    player_q = bfs(player_q)

    if not player_q:
        if can_escape:
            print(time + 1)
            break

        else:
            print("IMPOSSIBLE")
            break

    time += 1