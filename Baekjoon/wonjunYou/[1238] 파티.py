import heapq
import sys

INF = float("inf")

input = sys.stdin.readline

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    dis = [INF] * (N + 1)
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))
    return dis[end]


N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
t = 0
for i in range(1, N + 1):
    if i == X:
        continue
    t = max(t, dijkstra(i, X) + dijkstra(X, i))
print(t)