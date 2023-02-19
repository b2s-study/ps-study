import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def func(n, r, c):
    if n == 0:
        return 0

    half = 1 << (n - 1)

    if (r < half and c < half):
        return func(n - 1, r, c)

    elif (r < half and c >= half):
        return half * half + func(n - 1, r, c - half)

    elif (r >= half and c < half):
        return 2 * half * half + func(n - 1, r - half, c)

    return 3 * half * half + func(n - 1, r - half, c - half)

n, r, c = map(int, input().rstrip('\n').split())

print(func(n, r, c))