# 메모리 초과난 코드

# import sys, heapq

# input = sys.stdin.readline
# n = int(input())
# heap = []

# for i in range(n):
# 	num_list = list(map(int, input().split()))
	
# 	for j in num_list:
# 		heapq.heappush(heap, -j) # 최대 힙 구현
		
# for i in range(heap - 1):
# 	heapq.heappop(heap)
	
# print(-heap[0])

import sys
import heapq

input = sys.stdin.readline

heap = []
N = int(input().rstrip('\n'))

for _ in range(N): 
    num_list = map(int, input().split())

    for i in num_list:
        if len(heap) < N:   # 힙의 크기가 N 미만일 경우 추가
            heapq.heappush(heap, i)

        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

print(heap[0])


        
