import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis = [INF]*(N+1)
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
    return dis

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

res = min(d1[v1] + d2[v2] + d3[N], d1[v2] + d3[v1] + d2[N])

if res < INF:
    print(res)

else:
    print(-1)
