import sys

input = sys.stdin.readline

N = int(input().rstrip('\n'))

data = list(map(int, input().rstrip('\n').split()))

print(min(data), max(data))