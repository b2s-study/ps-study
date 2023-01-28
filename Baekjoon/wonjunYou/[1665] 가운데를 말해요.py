import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip('\n'))

small = []
big = []
result = []

for _ in range(n):
    number = int(input().rstrip('\n'))

    if len(small) == len(big):
        heapq.heappush(small, (-number, number))
    else:
        heapq.heappush(big, number)

    if big and small[0][1] > big[0]:
        left = heapq.heappop(small)[1]
        right = heapq.heappop(big)

        heapq.heappush(small, (-right, right))
        heapq.heappush(big, left)

    result.append(small[0][1])

print(*result)
