from collections import deque
import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().rstrip('\n').split())

max_dishes = 0

sushi = [int(input().rstrip('\n')) for _ in range(n)]

sushi += sushi

start = 0
end = k - 1

once = []

while (start < n):
    once = sushi[start:end+1]

    set_once = set(once)

    dishes = len(set_once)

    if c not in set_once:
        dishes += 1

    max_dishes = max(max_dishes, dishes)

    start += 1
    end += 1
print(max_dishes)
