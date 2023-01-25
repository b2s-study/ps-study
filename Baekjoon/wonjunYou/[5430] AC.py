from collections import deque
import sys

input = sys.stdin.readline

t = int(input().rstrip('\n'))

for _ in range(t):
    p = input().rstrip('\n')
    n = int(input().rstrip('\n'))

    numbers = deque(input().rstrip('\n')[1:-1].split(','))

    if n == 0:
        numbers = []

    is_reversed = False

    for idx in range(len(p)):
        if p[idx] == "D":
            if len(numbers) == 0:
                print("error")
                break

            if not is_reversed:
                numbers.popleft()
            else:
                numbers.pop()

        elif p[idx] == "R":
            if not is_reversed:
                is_reversed = True
            else:
                is_reversed = False
    else:
        if is_reversed:
            numbers.reverse()

        print("[" + ",".join(numbers) + "]")
