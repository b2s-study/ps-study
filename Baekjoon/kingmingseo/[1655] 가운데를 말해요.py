import sys
import heapq
input = sys.stdin.readline
loop = int(input())

left_heap = []
right_heap = []

for i in range (loop):
    value = int(input())

    if len(right_heap) == len(left_heap):
        heapq.heappush(left_heap, -value)

    else :
        heapq.heappush(right_heap, value)

    if right_heap and right_heap[0] < -left_heap[0]:
        leftValue = heapq.heappop(left_heap)
        rightValue = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -rightValue)
        heapq.heappush(right_heap, -leftValue)

    print(-left_heap[0])