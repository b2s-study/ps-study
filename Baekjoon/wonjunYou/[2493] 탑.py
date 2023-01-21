import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

towers = list(map(int, input().rstrip('\n').split()))

stack = []
result = [0] * n

for idx in range(len(towers)):
    while stack:
        if towers[stack[-1]] < towers[idx]:
            stack.pop()
        else:
            result[idx] = stack[-1] + 1
            break

    stack.append(idx)

print(*result)
