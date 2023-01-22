import sys

input = sys.stdin.readline

N = int(input().rstrip('\n'))

STAR_CHARACTER = '*'
ONE_SPACE = " "

for length in range(1, N + 1):
    print(ONE_SPACE * (N - length) + STAR_CHARACTER * (length))