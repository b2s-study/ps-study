import sys

input = sys.stdin.readline

STAR_CHARACTER = '*'

N = int(input().rstrip('\n'))

for length in range(N):
    print(STAR_CHARACTER * (length + 1))
