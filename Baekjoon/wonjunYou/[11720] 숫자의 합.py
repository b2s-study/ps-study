import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

result = 0

numbers = input().rstrip('\n')

for i in range(n):
    result += int(numbers[i])

print(result)