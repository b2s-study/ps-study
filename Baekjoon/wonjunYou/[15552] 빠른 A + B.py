import sys

input = sys.stdin.readline

T = int(input().rstrip('\n'))

for _ in range(T):
    A, B = map(int, input().rstrip('\n').split())

    print(A + B)