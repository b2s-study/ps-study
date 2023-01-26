import sys
import heapq

input = sys.stdin.readline

N = int(input())

# min_heap = MinHeap()
min_heap = []
for _ in range(N):
    value = int(input())
    if value == 0:
        # min_value = min_heap.pop()
        min_value = heapq.heappop(min_heap) if len(min_heap) != 0 else 0
        print(min_value)
        continue

    # min_heap.insert(value)
    heapq.heappush(min_heap, value)
