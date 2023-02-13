from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
    union = []

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    union.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<n):
                if not visited[nx][ny] and (L <= abs(world[nx][ny] - world[x][y]) <= R):
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    union.append((nx, ny))

    if len(union) == 1:
        return

    return union

def update(unions):
    for union in unions:
        people = 0
        country_count = len(union)

        # 새롭게 배분할 인구 계산하기
        for x, y in union:
            people += world[x][y]

        new_people = int(people / country_count)

        # 인구 업데이트
        for x, y in union:
            world[x][y] = new_people

# L <= 인구 <= R

# 연합의 인구수를 / 칸 수로 (소숫점 버리니까 INT
# 며칠동안 인구를 이동시키느냐. # 인구가 모두 같아지면 끝.

n, L, R = map(int, input().rstrip('\n').split())
world = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

day = 0
while True:
    visited = [[0] * n for _ in range(n)]
    unions = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = bfs(i, j)

                if union:
                    unions.append(union)

    if not unions:
        print(day)
        break

    update(unions)
    day += 1