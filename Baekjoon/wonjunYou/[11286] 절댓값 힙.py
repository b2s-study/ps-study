import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip('\n'))

arr = []

for _ in range(n):
    x = int(input().rstrip('\n'))

    if x == 0:
        if not arr:
            print("0")
            continue

        print(heapq.heappop(arr)[1])

    else:
        heapq.heappush(arr, (abs(x), x))