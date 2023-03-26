
import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for num in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

# 출발점과 도착점
A,B = map(int,input().split())

INF = 100000000
heap = []

def dijkstra(start):
    
    # 초기화
    dp = [INF]*(N+1)
    dp[start]=0
    
    heapq.heappush(heap,(0,start))
    
    while heap:
        
        wei, now = heapq.heappop(heap)
        if dp[now] < wei:
            continue
        
        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap,(next_wei,next_node))
    return dp

ans = dijkstra(A)
print(ans[B])
