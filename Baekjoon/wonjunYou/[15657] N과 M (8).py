import sys

input = sys.stdin.readline

def func(lens):
    if lens == m:
        print(*result)
        return

    for idx in range(len(numbers)):
        if lens > 0 and result[lens - 1] > numbers[idx]:
            continue

        result[lens] = numbers[idx]
        func(lens + 1)
        result[lens] = 0

n, m = map(int, input().rstrip('\n').split())
numbers = list(map(int, input().rstrip('\n').split()))

numbers.sort()

result = [0] * m

func(0)