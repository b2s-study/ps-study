import math
import sys
import heapq

input = sys.stdin.readline

t = int(input().rstrip('\n'))

for _ in range(t):
    m = int(input().rstrip('\n'))

    print(math.ceil(m / 2))

    small = []
    big = []
    result = []

    for _ in range(math.ceil(m / 10)):
        numbers = list(map(int, input().rstrip('\n').split()))

        for idx in range(len(numbers)):
            if len(small) == len(big):
                heapq.heappush(small, (-numbers[idx], numbers[idx]))

            else:
                heapq.heappush(big, numbers[idx])

            if big and small[0][1] > big[0]:
                left = heapq.heappop(small)[1]
                right = heapq.heappop(big)

                heapq.heappush(small, (-right, right))
                heapq.heappush(big, left)

            if (idx % 2 == 0):
                result.append(small[0][1])

        if (len(result) >= 10):
            print(*result)
            result.clear()

    print(*result)