import sys

input = sys.stdin.readline

N = int(input())
n_list = set(map(int, input().split()))
M = int(input())
m_list = list(map(int, input().split()))

for m_number in m_list:
  if m_number in n_list:
    print(1, end=" ")
  else:
    print(0, end=" ")