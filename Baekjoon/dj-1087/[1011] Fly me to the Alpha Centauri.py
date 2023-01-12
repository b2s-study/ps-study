# 처음, 마지막 = 1
# 두번째 = 1 or 2

# if distance == 1 -> 1
# if distance == 2 -> 1, 1 -> 2

# if distance == 3 -> 1, 1, 1 -> 3
# if distance == 4 -> 1, 2, 1 -> 3

# if distance == 5 -> 1, 2, 1, 1 -> 4
# if distance == 6 -> 1, 2, 2, 1 -> 4

# if distance == 7 -> 1, 2, 1, 2, 1 -> 5
# if distance == 8 -> 1, 2, 2, 2, 1 -> 5
# if distance == 9 -> 1, 2, 3, 2, 1 -> 5

# if distance == 10 -> 1, 2, 3, 1, 2, 1 -> 6
# if distance == 11 -> 1, 2, 3, 2, 2, 1 -> 6
# if distance == 12 -> 1, 2, 3, 3, 2, 1 -> 6

# if distance == 13 -> 1, 2, 3, 1, 3, 2, 1 -> 7
# if distance == 14 -> 1, 2, 3, 2, 3, 2, 1 -> 7
# if distance == 15 -> 1, 2, 3, 3, 3, 2, 1 -> 7
# if distance == 16 -> 1, 2, 3, 4, 3, 2, 1 -> 7

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  x, y = map(int, input().split())
  distance = y - x

  break_point = 0
  step = 0
  while(True):
    if (break_point >= distance):
      break

    step += 1
    break_point += 2*step

  point = (break_point + break_point - 2*step) / 2
  if distance > point:
    print(2*step)
  else:
    print(2*step - 1)

  