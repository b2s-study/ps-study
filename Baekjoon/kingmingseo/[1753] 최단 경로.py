import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int,input().split())
start = int(input())
distance =[INF for _ in range(V + 1)]
data = [[] for _ in range (V + 1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    data[u].append((v, w))

q = []
def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q,(0, start))

    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for search_node, weight in data[cur]:
            cost = dist + weight

            if cost < distance[search_node]:
                distance[search_node] = cost
                heapq.heappush(q,(cost, search_node))


dijkstra(start)

for idx in range (1,len(distance)):
    if distance[idx] != INF:
        print(distance[idx])
    else:
        print("INF")

