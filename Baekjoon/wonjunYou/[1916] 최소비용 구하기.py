import heapq
import sys

input = sys.stdin.readline

INF = float("inf")

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

visited = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

def dijkstra(x):
    q = []
    heapq.heappush(q, (0, x))
    visited[x] = 0

    while q:
        d, x = heapq.heappop(q)

        if visited[x] < d:
            continue

        for w, x in graph[x]:
            nd = d + w

            if visited[x] > nd:
                heapq.heappush(q, (nd, x))
                visited[x] = nd

dijkstra(start)

print(visited[end])