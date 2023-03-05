import sys

input = sys.stdin.readline

def func(lens):
    if lens == m:
        print(*result)
        return

    for idx in range(len(numbers)):
        if not visited[idx]:
            if lens > 0 and result[lens - 1] > numbers[idx]:
                continue

            visited[idx] = 1
            result[lens] = numbers[idx]
            func(lens + 1)
            visited[idx] = 0

n, m = map(int, input().rstrip('\n').split())
numbers = list(map(int, input().rstrip('\n').split()))

numbers.sort()

result = [0] * m
visited = [0] * (n + 1)

func(0)

