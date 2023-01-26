import sys
import heapq

input = sys.stdin.readline

N = int(input())

absolute_heap = []
for _ in range(N):
    number = int(input())
    if number == 0:
        node = heapq.heappop(absolute_heap) if len(
            absolute_heap) != 0 else (0, 0)
        print(node[1])
        continue

    node = (abs(number), number)
    heapq.heappush(absolute_heap, node)
