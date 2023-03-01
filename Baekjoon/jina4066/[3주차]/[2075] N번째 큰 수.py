import sys, heapq

input = sys.stdin.readline
n = int(input())
heap = []

for i in range(n):
	num_list = list(map(int, input().split()))
	
	for j in num_list:
		heapq.heappush(heap, -j) # 최대 힙 구현
		
for i in range(heap - 1):
	heapq.heappop(heap)
	
print(-heap[0])