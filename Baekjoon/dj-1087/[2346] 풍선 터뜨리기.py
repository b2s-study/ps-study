import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
move_point_list = list(map(int, input().split()))
balloon_deque = deque(enumerate(move_point_list))

while (True):
    if len(balloon_deque) == 0:
        break

    balloon = balloon_deque.popleft()

    balloon_number = balloon[0] + 1
    print(balloon_number, end=" ")

    move_point = 0
    if (balloon[1] > 0):
        move_point = -1 * (balloon[1] - 1)
    else:
        move_point = -1 * balloon[1]
    balloon_deque.rotate(move_point)
