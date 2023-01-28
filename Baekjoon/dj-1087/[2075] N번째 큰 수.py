import sys
import heapq

input = sys.stdin.readline

N = int(input())
mean_heap = []

for _ in range(N):
    row = list(map(int, input().split()))

    if len(mean_heap) == 0:
        for number in row:
            heapq.heappush(mean_heap, number)
        continue

    for number in row:
        if number < mean_heap[0]:
            continue
        heapq.heappush(mean_heap, number)
        heapq.heappop(mean_heap)

print(mean_heap[0])
