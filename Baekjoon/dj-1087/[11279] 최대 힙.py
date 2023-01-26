import sys
import heapq

input = sys.stdin.readline

N = int(input())
mean_heap = []

for _ in range(N):
    count = int(input())
    heapq.heappush(mean_heap, count)

total_count = 0
while (True):
    if len(mean_heap) <= 1:
        break

    A = heapq.heappop(mean_heap)
    B = heapq.heappop(mean_heap)

    total_count += A + B
    heapq.heappush(mean_heap, A + B)

print(total_count)
