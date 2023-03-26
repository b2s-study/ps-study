import sys
import heapq


def dijkstra(start, end):
    cost_list = [sys.maxsize] * (N+1)
    pq = []

    cost_list[start] = 0
    heapq.heappush(pq, [0, start, [start]])

    while pq:
        weight, vertex, path = heapq.heappop(pq)
        if vertex == end:
            return [weight, path]

        for nw, nv in graph[vertex]:
            nc = weight + nw
            if cost_list[nv] <= nc:
                continue
            cost_list[nv] = nc
            heapq.heappush(pq, (nc, nv, path + [nv]))


input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
start, end = map(int, input().split())

cost, path = dijkstra(start, end)
print(cost)
print(len(path))
print(*path)
