import sys
import heapq
from collections import deque


def dijkstra(start, graph):
    distance = [sys.maxsize for _ in range(N)]
    pq = []

    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        weight, vertex = heapq.heappop(pq)
        if distance[vertex] < weight:
            continue
        for nv, nw in graph[vertex]:
            nd = nw + weight
            if distance[nv] <= nd:
                continue
            distance[nv] = nd
            heapq.heappush(pq, (nd, nv))

    return distance


def bfs(end, back_graph, distance) -> set:
    # search direction: end -> start
    # return paths set that should remove
    visited = [[False] * N for _ in range(N)]
    q = deque()
    remove_paths = set()
    q.append(end)

    while q:
        current = q.popleft()
        for (prev, cost) in back_graph[current]:
            if visited[current][prev]:
                continue
            if distance[current] == distance[prev]+cost:
                # 바로 graph에 사용할 수 있게! 순서를 바꿔 원래 그래프의 from to 방향대로 넣음
                remove_paths.add((prev, current))
                q.append(prev)
                if prev == S:
                    continue
                else:
                    visited[current][prev] = True
    return remove_paths


sys.setrecursionlimit(10**6)
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        break
    S, D = map(int, input().split())

    graph = [[] for _ in range(N)]
    back_graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        back_graph[v].append((u, p))

    distance = dijkstra(S, graph)
    remove_paths = bfs(D, back_graph, distance)

    new_graph = [[] for _ in range(N)]
    for u in range(N):
        for (v, p) in graph[u]:
            if (u, v) in remove_paths:
                continue
            new_graph[u].append((v, p))

    distance = dijkstra(S, new_graph)
    if distance[D] == sys.maxsize:
        print(-1)
    else:
        print(distance[D])
