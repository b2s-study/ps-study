import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int, input()))
sum = 0

for i in range(N):
    sum += numList[i]

print(sum)
