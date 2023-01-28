import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
card = deque()

for i in range (1,n+1):
    card.append(i)

while (len(card) > 1):
    card.popleft()
    card.rotate(-1)

print(card.popleft())