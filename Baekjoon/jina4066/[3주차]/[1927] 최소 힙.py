import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip('\n'))

heap = []

for _ in range(N):
    x = int(input().rstrip('\n'))
    
    if x == 0: # 배열에서 가장 작은 값 출력 후 그 값을 배열에서 제거
        if not heap: # 배열이 비어 있는 경우 -> 0 출력
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)

