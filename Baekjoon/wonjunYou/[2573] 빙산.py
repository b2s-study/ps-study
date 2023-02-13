import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**4)

def melt_ice():
    ice = [[0] * m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            if iceberg[x][y] > 0:
                ice[x][y] = 1

                for i in range(4):
                    if iceberg[x][y] == 0:
                        break

                    nx = x + dx[i]
                    ny = y + dy[i]

                    if (0<=nx<n and 0<=ny<m):
                        if iceberg[nx][ny] == 0 and ice[nx][ny] == 0:
                            iceberg[x][y] -= 1

def check_iceberg():
    visited = [[0] * m for _ in range(n)]
    is_activated = False

    for x in range(n):
        for y in range(m):
            if iceberg[x][y] > 0:
                if is_activated and not visited[x][y]:
                    print(day)
                    return True

                elif not is_activated:
                    is_activated = True
                    dfs(x, y, visited)

    if not is_activated:
        print(0)
        return True

    return False
def dfs(x, y, visited):
    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<n and 0<=ny<m):
            if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                dfs(nx, ny, visited)

# check_bfs
# 1. 있는데 모두 연결됨.
# 2. 있는데 분리됨.

# 만약에 값 찾았는데, is_activated = True인 경우 결과 출력. 아니면 dfs 실행
# 3. 모두 녹아서 없어짐. is_activated = False인 경우 : 0 출력하도록.

n, m = map(int, input().rstrip('\n').split())

iceberg = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

day = 0
while True:
    melt_ice()
    day += 1
    has_result = check_iceberg()

    if has_result:
        break