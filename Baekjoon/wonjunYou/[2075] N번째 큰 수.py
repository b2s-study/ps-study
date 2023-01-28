import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip('\n'))

arr = []

for _ in range(n):
    data = list(map(int, input().rstrip('\n').split()))

    if not arr:
        for number in data:
            heapq.heappush(arr, number)

    else:
        for number in data:
            if arr[0] < number:
                heapq.heappop(arr)
                heapq.heappush(arr, number)

print(arr[0])