import sys

input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())  # 노드 수 n, 간선 수 m 입력 받기

edges = []    # 모든 간선에 대한 정보를 담는 리스트 생성
dist = [INF] * (n+1)

#그래프 생성
for _ in range(m): 
    u, v, w = map(int, input().split())  # 노드, 인접 노드, 가중치
    edges.append((u, v, w))

#벨만 포드 알고리즘
def bf(start) : 
    dist[start] = 0
    for i in range(n):  
        for j in range(m):
            node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost 
                #n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1 :  # n-1번 이후 반복에도 값이 갱신되면 음수 순환 존재
                    return True
    return False

#벨만 포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        if dist[i] == INF: #도달할 수 없는 경우 -1 출력
            print('-1')
        else: #도달할 수 있는 경우 거리를 출력
            print(dist[i])