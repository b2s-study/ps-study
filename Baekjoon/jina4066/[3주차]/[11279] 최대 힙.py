import sys
import heapq

input = sys.stdin.readline

heap = []

N = int(input().rstrip('\n'))

for _ in range(N):
    x = int(input().rstrip('\n'))

    if x == 0:
        if not heap:
            print(0)
        else:
            print((-1) * heapq.heappop(heap))
    else:
        heapq.heappush(heap, (-1) * x)
