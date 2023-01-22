import sys

input = sys.stdin.readline

T = int(input().rstrip('\n'))

for _ in range(T):
    x, y = map(int, input().rstrip('\n').split())
    diff = int(y - x)

    position = 0
    step = 1
    times = 0

    while (position < diff):
        times += 1
        position += step
        if (times % 2 == 0):
            step += 1

    print(times)