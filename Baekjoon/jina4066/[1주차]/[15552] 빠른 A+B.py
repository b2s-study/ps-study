import sys

input = sys.stdin.readline

T = int(input())
list = []

for i in range(T):
    A, B = map(int, input().strip().split())
    list.append(A+B)
  
for i in range(T):
    print(list[i])
  
