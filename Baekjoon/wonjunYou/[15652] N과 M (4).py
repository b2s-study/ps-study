import sys

input = sys.stdin.readline

def func(lens):
    if lens == m:
        print(*result)
        return

    for idx in range(1, n+1):
        if lens > 0 and result[lens - 1] > idx:
            continue

        result[lens] = idx
        func(lens + 1)
        result[lens] = 0

n, m = map(int, input().rstrip('\n').split())

result = [0] * m

func(0)