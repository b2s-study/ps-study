import sys

input = sys.stdin.readline

def func(lens):
    if lens == m:
        print(*result)
        return

    prev = -1
    for idx in range(len(numbers)):
        if not visited[idx] and prev != numbers[idx]:
            result[lens] = numbers[idx]
            prev = numbers[idx]
            visited[idx] = 1
            func(lens + 1)
            visited[idx] = 0

n, m = map(int, input().rstrip('\n').split())
numbers = list(map(int, input().rstrip('\n').split()))

numbers.sort()

result = [0] * m
visited = [0] * n

func(0)