
import sys
import heapq
input = sys.stdin.readline

N,E = map(int,input().split())

graph = [[] for _ in range(N+1)]

for num in range(1,E+1):
    u,v,w = map(int,input().split())
    # 양방향 모두 넣어주기
    graph[u].append((w,v))
    graph[v].append((w,u))

# 무조건 지나야 하는 노드 A,B
A,B = map(int,input().split())

INF = sys.maxsize
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

dp1 = dijkstra(1)
dp2 = dijkstra(A)
dp3 = dijkstra(B)
# 1->A->B->N 일수도 있고 (case1)
# 1->B->A-> 일수도 있다 !! 두 가지 경우 모두 구하기 (case2)

# min(case1,case2)
ans = min(dp1[A]+dp2[B]+dp3[N],dp1[B]+dp2[N]+dp3[A])
print( ans if ans < INF else -1)