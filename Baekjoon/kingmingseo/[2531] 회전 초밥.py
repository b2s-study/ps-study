import itertools
import sys
from collections import deque

input = sys.stdin.readline

dish , sushi, eat, coupon = map(int,input().split())
sushi_list = deque()

for _ in range(dish):
    sushi_list.append(int(input()))

answer = 0

for i in range(dish):
    slice_list = list(itertools.islice(sushi_list,0,eat))

    temp1 = set(slice_list)

    if len(temp1) + 1 > answer and coupon not in temp1:
        answer = len(temp1) + 1

    elif len(temp1) > answer:
        answer = len(temp1)

    sushi_list.rotate(-1)

print(answer)




