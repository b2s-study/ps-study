
# 답안 참고 !! 어렵당,,,
# 여러 학생들 중 가장 많은 시간을 소비하는 학생 구하기 

import sys
import heapq
input = sys.stdin.readline

N,M,X = map(int,input().split())

# start -> X
INF = sys.maxsize

graph = [[] for _ in range(N+1)]
heap = []

# graph에 요소 삽입
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    


def dijkstra(start):
    dp = [INF]*(N+1) 
    # 시작점 초기화 
    dp[start]=0
    heapq.heappush(heap,(0,start))
    
    while heap:
        wei, now = heapq.heappop(heap)
        
        if dp[now] < wei:
            continue
        
        for w, next_node in graph[now]:
            next_wei = wei + w
            
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei,next_node))
    return dp


# 집 돌아갈 때의 거리   
ans = dijkstra(X)

for house in range(1,N+1):
    if house != X:
        res = dijkstra(house)
        ans[house] += res[X]
    

print(max(ans[1:]))
