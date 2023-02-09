import sys
from collections import deque


def dfs(v):
    result = [v]
    visited[v] = 1
    for i in range(1, len(graph[v])):
        if (visited[i] == 1) or (graph[v][i] == 0):
            continue
        sub_result = dfs(i)
        result.extend(sub_result)

    return result


def bfs(v):
    visited[v] = 1
    q = deque([v])

    result = []
    while (q):
        value = q.popleft()
        result.append(value)
        for i in range(1, len(graph[value])):
            if (visited[i] == 1) or (graph[value][i] == 0):
                continue
            visited[i] = 1
            q.append(i)
    return result


input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1][n2] = graph[n2][n1] = 1

result_dfs = dfs(V)
print(*result_dfs)

visited = [0] * (N+1)
result_bfs = bfs(V)
print(*result_bfs)
