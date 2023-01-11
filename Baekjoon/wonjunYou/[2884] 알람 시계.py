import sys

input = sys.stdin.readline

H, M = map(int, input().rstrip('\n').split())

MAX_HOUR = 24
MAX_MINUTE = 60

if (M < 45):
    M = (MAX_MINUTE + M) - 45

    if (H == 0):
        H = MAX_HOUR - 1

    else:
        H = H - 1

else:
    M = M - 45

print(H, M)
