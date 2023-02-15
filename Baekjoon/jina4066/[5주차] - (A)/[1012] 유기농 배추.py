from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x, y))

    #방문 노드 0으로 표시
    graph[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<m):
                if graph[nx][ny] == 1:
                    q.append((nx, ny))
                    graph[nx][ny] = 0

    return count

T = int(input().rstrip('\n'))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# T만큼 배추밭의 가로길이, 세로길이, 배추가 심어져 있는 위치의 개수 입력받는다.
for _ in range(T):
    m, n, k = map(int, input().rstrip('\n').split())

    graph = [[0] * m for _ in range(n)]
    count = 0

    # 입력
    for _ in range(k):
        x, y = map(int, input().rstrip('\n').split())
        graph[y][x] = 1

    # 시작점 탐색
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                bfs(x, y)
                count += 1
    # 출력
    print(count)

    

    