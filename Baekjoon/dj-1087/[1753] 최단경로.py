import sys
import heapq


def dijkstra(k):
    distance = [sys.maxsize] * (V+1)
    pq = []

    distance[k] = 0
    heapq.heappush(pq, (0, k))

    while pq:
        w, v = heapq.heappop(pq)
        for nv, nw in graph[v]:
            nd = nw + w
            if distance[nv] <= nd:
                continue
            distance[nv] = nd
            heapq.heappush(pq, (nd, nv))

    return distance


input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = dijkstra(K)
for d in distance[1:]:
    print(d if d != sys.maxsize else "INF")
