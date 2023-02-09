import sys

input = sys.stdin.readline

str = list(input().split())

cnt = 0

for _ in range(len(str)): 
    cnt += 1

print(cnt)
