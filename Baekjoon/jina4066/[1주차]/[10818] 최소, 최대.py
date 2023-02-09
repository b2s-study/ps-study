import sys

input = sys.stdin.readline

N = int(input())
str = list(map(int, input().split()))

min = str[0]
max = str[0]

for i in range(N):

    if min > str[i]:
        min = str[i]
    if max < str[i]:
        max = str[i]

print(min, max)
