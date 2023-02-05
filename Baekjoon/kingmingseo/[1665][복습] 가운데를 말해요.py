import sys
import heapq
input = sys.stdin.readline
left_heap = []
right_heap = []

N = int(input())

for i in range(N):
    value = int(input())

    if len(left_heap) == 0 or len(left_heap) <= len(right_heap):
        heapq.heappush(left_heap, -value)

    else:
        heapq.heappush(right_heap, value)
    if right_heap and -left_heap[0] > right_heap[0] :
        left_temp = heapq.heappop(left_heap)
        right_temp = heapq.heappop(right_heap)
        heapq.heappush(left_heap , -right_temp)
        heapq.heappush(right_heap, -left_temp)

    print(-left_heap[0])






