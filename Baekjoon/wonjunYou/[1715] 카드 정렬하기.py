import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip('\n'))
arr = []

total = 0

for _ in range(n):
    number = int(input().rstrip('\n'))

    heapq.heappush(arr, number)

for _ in range(n-1):
    left = heapq.heappop(arr)
    right = heapq.heappop(arr)

    total += (left + right)
    heapq.heappush(arr, (left + right))

print(total)