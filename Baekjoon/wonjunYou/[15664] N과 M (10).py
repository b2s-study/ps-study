import sys

input = sys.stdin.readline

def func(lens):

    if lens == m:
        print(*result)
        return

    prev = -1
    for idx in range(len(numbers)):
        if lens > 0 and result[lens - 1] > numbers[idx]:
            continue

        if not visited[idx] and prev != numbers[idx]:
            visited[idx] = 1
            result[lens] = numbers[idx]
            prev = numbers[idx]
            func(lens + 1)
            visited[idx] = 0

n, m = map(int, input().rstrip('\n').split())
numbers = list(map(int, input().rstrip('\n').split()))

numbers.sort()

visited = [0] * n
result = [0] * m

func(0)