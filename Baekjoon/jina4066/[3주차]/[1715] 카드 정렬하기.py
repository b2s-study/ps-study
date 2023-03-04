import sys
import heapq

input = sys.stdin.readline

heap = [] # 카드 묶음 최소 힙 정렬

N = int(input().rstrip('\n'))

for _ in range(N):
    num = int(input().rstrip('\n'))

    heapq.heappush(heap, num)

result = 0

if len(heap) == 1:
    print(result)

else:
    for _ in range(N-1):
        previous = heapq.heappop(heap)
        current = heapq.heappop(heap)

        result += previous + current
        heapq.heappush(heap, previous + current)

    print(result)
    