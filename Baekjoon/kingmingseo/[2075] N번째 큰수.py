import heapq
import sys
input = sys.stdin.readline

count = int(input())
min_heap = []

for i in range(count):
    temp = list(map(int,input().split()))

    if not min_heap:
        for j in range(count):
            heapq.heappush(min_heap ,temp[j])

    else:
        for j in range(count):
            if min_heap[0] < temp[j]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, temp[j])


print(min_heap[0])


