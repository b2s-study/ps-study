import sys


def find(N, r, c):
    # print(r, c)
    if N == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0:
            return 1
        elif c == 0:
            return 2
        else:
            return 3

    # if 2^N = 8 -> mid = 4
    mid = 2**(N-1)
    area = (2**(N-1))**2
    if (r < mid) and (c < mid):
        return find(N-1, r, c)
    elif r < mid:
        return area + find(N-1, r, c - mid)
    elif c < mid:
        return 2*area + find(N-1, r - mid, c)
    else:
        return 3*area + find(N-1, r - mid, c - mid)


input = sys.stdin.readline

N, r, c = map(int, input().split())
order = find(N, r, c)
print(order)
