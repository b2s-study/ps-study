from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

balloons = deque(list(map(int, input().rstrip('\n').split())))
balloon_numbers = deque([i for i in range(1, n+1)])

result = []

for order in range(1, n+1):
    result.append(balloon_numbers.popleft())
    step = balloons.popleft()

    if step > 0:
        balloons.rotate(-(step - 1))
        balloon_numbers.rotate(-(step - 1))

    else:
        balloons.rotate(-step)
        balloon_numbers.rotate(-step)

print(*result)

