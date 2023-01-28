# https://www.acmicpc.net/problem/2075




# 풀이 1. 메모리 초과 -> 모든 수를 힙에 넣는 과정을 생략해야 할 듯?
# import sys
# import heapq
# # 힙에 모두 저장해서 N번째 큰 수 찾기
# N = int(sys.stdin.readline())

# heap = []
# for _ in range(N): 
#     x_list = list(map(int,sys.stdin.readline().rstrip().split()))

#     for x in x_list:
#         heapq.heappush(heap,-x)

# # print(heap)
# for _ in range(N-1):
#     heapq.heappop(heap)

# print(-heapq.heappop(heap))



# 풀이 2. 메모리 초과 해결하기 -> heap 칸 수를 줄이기 

import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for _ in range(N): 
    x_list = list(map(int,sys.stdin.readline().rstrip().split()))

    # push하기
    for x in x_list:
        # heap의 크기를 N으로 제한한다. -> 나중에 그래야 N번째 큰 수가 heap[0](heap 중에 가장 작은 수)로 있게 된다. 
        if len(heap)<N:
            heapq.heappush(heap,x)
        # heap요소 중 가장 작은수 보다 새로들어오는 요소가 더 크면 pop & push 해준다. -> 크기유지  
        elif heap[0]<x:   
            heapq.heappop(heap)
            heapq.heappush(heap,x) 
# 최종적으로 N번째 큰 수가 heap의 가장 작은 수 heap[0]에 위치하게 된다. 
print(heap[0])


# 질문사항 -> 메모리 계산하는 법?