from collections import deque
import sys

input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


t = int(input().rstrip('/')) 
result_list = []

def make_graph(m, n, k):
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    return graph

def bfs(y, x):

    queue = deque([])
    queue.append([y, x])

    while queue:
        y, x = queue.pop()
        for d in range(4):
            xx = dx[d] + x
            yy = dy[d] + y
            if 0 <= xx < m and 0 <= yy < n:
                if graph[yy][xx] == 1:
                    graph[yy][xx] = 0
                    queue.append([yy, xx])


for _ in range(t):
    result = 0
    m, n, k = map(int, input.split()) # m:가로, n:세로
    graph = make_graph(m, n, k)
    for i in range(n): # 세로
        for j in range(m): # 가로
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1
    result_list.append(result)

print(*result_list, sep='\n')
