import sys

input = sys.stdin.readline

n, s = map(int, input().rstrip('\n').split())
numbers = list(map(int, input().rstrip('\n').split()))

INF = 100000001

start, end = 0, 0
total = numbers[0]
result = INF

while (start < n):
    if ((end >= n-1) and (total < s)):
        break

    if (total < s):
        end += 1
        total += numbers[end]

    else:
        result = min(result, (end - start + 1))
        total -= numbers[start]
        start += 1

if (result == INF):
    print(0)

else:
    print(result)