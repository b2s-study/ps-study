import sys
import heapq


def dijkstra(n, k):
    distance = [[] for _ in range(n+1)]
    pq = []

    heapq.heappush(distance[1], 0)
    heapq.heappush(pq, (0, 1))
    while pq:
        weight, vertex = heapq.heappop(pq)
        for nv, nw in graph[vertex]:
            nd = nw + weight
            heapq.heappush(distance[nv], -1 * nd)
            # print(distance)
            if len(distance[nv]) > k:
                heapq.heappop(distance[nv])
                continue
            heapq.heappush(pq, (nd, nv))

    return distance


input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = dijkstra(n, k)
for i in range(1, n+1):
    if (len(distance[i]) < k):
        print(-1)
    else:
        print(-1 * distance[i][0])
