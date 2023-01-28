import sys
from collections import deque

def shuffle(card_deq):
  if len(card_deq) == 1:
    return card_deq.pop()

  card_deq.popleft()
  card_deq.rotate(-1)

  return shuffle(card_deq)

input =  sys.stdin.readline

N = int(input())
card_deq = deque([x for x in range(1, N+1)])
result = 0

while(True):
  if len(card_deq) == 1:
    result = card_deq.pop()
    break

  card_deq.popleft()
  card_deq.rotate(-1)

print(result)