import sys
import heapq

input = sys.stdin.readline
V, E = map(int,input().split())
K = int(input())

# dp & graph 
INF = sys.maxsize
dp = [INF]*(V+1)
heap = []
graph = [[] for _ in range(V+1)]

# graph 삽입
for _ in range(E):
    u, v, w = map(int,input().split())
    # (가중치,목적지 노트) 형태로 저장
    graph[u].append((w,v))

def Dijkstra(start):
    # 초기화
    dp[start]=0
    heapq.heappush(heap,(0,start))
    
    # 힙에 원소가 없을 때까지
    while heap:
        # 현재 원소 받아옴
        wei, now = heapq.heappop(heap)
        
        # 현재 테이블과 비교하여 필요한(가중치가 더 작은) 튜플이면 
        if dp[now] >= wei:
        
            # 현재 정점까지의 가중치 wei + 현재 정점에서 다음 정점(next_node) 까지의 가중치 w => 다음 노드까지의 가중치
            for w, next_node in graph[now]:
                next_wei = w + wei
                # 다음 노드까지의 가중치(next_wei)가 현재 기록된 값보다 적으면 조건 성립
                if next_wei < dp[next_node]:
                    dp[next_node] = next_wei
                    # 다음 점까지의 가중치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입
                    heapq.heappush(heap,(next_wei,next_node))
                
Dijkstra(K)
    
for i in range(1,V+1):
    print('INF' if dp[i]==INF else dp[i])