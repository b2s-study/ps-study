import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
A.sort()

answer = 2000000001
left, right = 0, 1
while (True):
    if (left > right) or (right >= len(A)):
        break

    diffrence = A[right] - A[left]
    if diffrence < M:
        right += 1
        continue

    answer = min(answer, diffrence)
    left += 1

print(answer)
