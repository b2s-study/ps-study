import sys
import heapq
input = sys.stdin.readline

input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int,input().split())
data =[[] for _ in range(N + 1)]
flag = [False for _ in range (N + 1)]


for _ in range(E):
    a, b, c = map(int,input().split())
    data[a].append((b,c))
    data[b].append((a,c))

v1, v2 = map(int,input().split())
q = []
def dijkstra(start):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, cur = heapq.heappop(q)
        for search_node, weight in data[cur]:
            cost = dist + weight

            if cost < distance[search_node]:
                distance[search_node] = cost
                heapq.heappush(q, (cost, search_node))
    return distance

one_v1 = dijkstra(1)
v1_v2 = dijkstra(v1)
v2_v1 = dijkstra(v2)

answer = min((one_v1[v1] + v1_v2[v2] + v2_v1[N]),(one_v1[v2] + v2_v1[v1] + v1_v2[N]))

if answer >= INF:
    print(-1)
else:
    print(answer)



