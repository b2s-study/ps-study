import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())

numbers = []

for _ in range(n):
    number = int(input().rstrip('\n'))
    numbers.append(number)

numbers.sort()

start, end = 0, 0
result = float('inf')

while (start < n and end < n):
    if numbers[end] - numbers[start] < m:
        end += 1

    else:
        result = min(result, (numbers[end] - numbers[start]))
        start += 1

print(result)