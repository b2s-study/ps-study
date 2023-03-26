import sys
import heapq
input= sys.stdin.readline
INF = sys.maxsize
N = int(input())
M = int(input())
data = [[] for _ in range(N + 1)]
path_data = [i for i in range(N + 1)]
distance = [INF for _ in range (N + 1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    data[a].append((b,c))

start, end = map(int,input().split())

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
                path_data[search_node] = cur

dijkstra(start)
print(distance[end])
path = []
temp = end
while True:
    path.append(temp)
    if temp == path_data[temp]:
        break
    temp = path_data[temp]
print(len(path))
path.reverse()
print(*path)