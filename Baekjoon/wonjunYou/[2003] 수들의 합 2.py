import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())
numbers = list(map(int, input().rstrip('\n').split()))

total = numbers[0]
start, end = 0, 0
result = 0

while (start < n):
    if total == m:
        result += 1
        total -= numbers[start]
        start += 1

    if end == n - 1 and total < m:
        break

    elif total < m:
        end += 1
        total += numbers[end]

    elif total > m:
        total -= numbers[start]
        start += 1

print(result)