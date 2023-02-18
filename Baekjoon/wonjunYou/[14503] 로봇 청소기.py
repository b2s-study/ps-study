import sys

input = sys.stdin.readline

def turn(head):
    return (head + 3) % 4

def dfs(x, y, head):
    global count

    if room[x][y] == 0:
        count += 1
        room[x][y] = -1

    for _ in range(4):
        head = turn(head)
        nx = x + d[head][0]
        ny = y + d[head][1]

        if room[nx][ny] == 0:
            dfs(nx, ny, head)
            return

    nx = x - d[head][0]
    ny = y - d[head][1]

    if room[nx][ny] != 1:
        dfs(nx, ny, head)

    return

n, m = map(int, input().rstrip('\n').split())

robot_x, robot_y, head = map(int, input().rstrip('\n').split())

room = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

# 북 -> 서 -> 남 -> 동
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

count = 0
dfs(robot_x, robot_y, head)

print(count)