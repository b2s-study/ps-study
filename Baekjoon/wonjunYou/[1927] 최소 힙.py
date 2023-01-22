import heapq
import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

arr = []

for _ in range(n):
    x = int(input().rstrip('\n'))

    if x == 0:
        if not arr:
            print("0")
            continue

        print(heapq.heappop(arr))

    else:
        heapq.heappush(arr, x)