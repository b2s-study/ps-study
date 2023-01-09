import sys

input = sys.stdin.readline

data = []

for _ in range(10):
    number = int(input().rstrip('\n'))
    rest = number % 42
    data.append(rest)

print(len(set(data)))