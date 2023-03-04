import sys

input = sys.stdin.readline

def func(lens):

    if lens == m:
        print(*result)
        return

    prev = -1
    for idx in range(len(numbers)):
        if prev != numbers[idx]:
            result[lens] = numbers[idx]
            prev = numbers[idx]
            func(lens + 1)
            result[lens] = 0

n, m = map(int, input().rstrip('\n').split())
numbers = list(map(int, input().rstrip('\n').split()))

numbers.sort()

result = [0] * m

func(0)