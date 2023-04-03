import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n = int(input())  # 도시의 개수 n개
m = int(input())  # 버스의 개수 m개

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())  # 출발 도시의 번호, 도착지의 도시 번호, 버스 비용
    graph[a].append((b, c))

start, end = map(int, input().split())  # 구하고자 하는 출발 도시번호, 도착 도시 번호

# 가장 가까운 노드를 기록
nearnest = [start] * (n + 1)
distance = [INF] * (n + 1)

q = [(0, start)]

while q:
    dist, now = heapq.heappop(q)

    # 만약 현재까지 기록된 거리보다 큰 거리로 방문하려고 한다면, 무시
    if dist > distance[now]:
        continue
    
    # next = 다음 방문할 노드의 번호, nextDist = 현재 노드에서 다음 노드까지의 거리(가중치)
    for next, nextDist in graph[now]:
        cost = nextDist + dist
        
        #만약 cost가 distance[next]보다 작으면 갱신
        if cost < distance[next]:
            distance[next], nearnest[next] = cost, now

            heapq.heappush(q, (cost, next))
    
ans = []
tmp = end

while tmp != start:
    ans.append(str(tmp))
    tmp = nearnest[tmp]

ans.append(str(start))
ans.reverse()

print(distance[end])
print(len(ans))
print(" ".join(ans))