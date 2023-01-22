import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

result = (n * (n + 1)) // 2

print(result)