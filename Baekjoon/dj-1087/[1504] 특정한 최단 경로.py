import sys
import heapq


def visited_all(points: dict):
    for visited in points.values():
        if not visited:
            return False
    return True


def dijkstra(start):
    global points, graph, N, v1, v2

    distance = [sys.maxsize] * (N+1)
    pq = []
    result = sys.maxsize

    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        weight, vertex = heapq.heappop(pq)
        if vertex in points and points[vertex] == False:
            points[vertex] = True
            # print(vertex, weight)
            result = min(result, weight + dijkstra(vertex))
            points[vertex] = False

        if vertex == N and visited_all(points):
            # print(vertex, weight)
            return weight

        for nw, nv in graph[vertex]:
            nd = weight + nw
            if distance[nv] <= nd:
                continue
            distance[nv] = nd
            heapq.heappush(pq, (nd, nv))

    return result


input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

for i in range(1, N+1):
    graph[i].sort()

v1, v2 = map(int, input().split())
points = {v1: False, v2: False}

result = dijkstra(1)
print(result if result != sys.maxsize else -1)
