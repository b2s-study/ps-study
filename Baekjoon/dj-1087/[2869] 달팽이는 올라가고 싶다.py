import sys

input = sys.stdin.readline

A, B, V = map(int,input().split())
days = (V - B)//(A - B)

if (V - B)%(A - B) != 0:
  print(days+1)
else:
  print(days)