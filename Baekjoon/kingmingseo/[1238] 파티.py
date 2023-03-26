import sys
import heapq
import copy
input = sys.stdin.readline
INF = sys.maxsize

N, M ,X = map(int,input().split())
data = [[] for _ in range(M+1)]
distance = [INF for _ in range(N+1)]
distance[0] = 0
q= []
answer = []
for i in range(M):
    start, end , weight = map(int,input().split())
    data[start].append((end,weight))
def djikstra(start):
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q :
        dist, cur = heapq.heappop(q)
        for search_node, weight in data[cur]:
            cost = dist + weight

            if cost < distance[search_node]:
                distance[search_node] = cost
                heapq.heappush(q,(cost,search_node))

djikstra(X)
dist2 = [0]
dist3 = distance.copy()
max_value = -sys.maxsize

for i in range(1, N+1):
    distance = [INF for _ in range(N+1)]
    distance[0] = 0
    djikstra(i)
    dist2.append(distance[X])

for i in range(1,N):
    max_value = max(max_value,dist2[i] + dist3[i])
print(max_value)
