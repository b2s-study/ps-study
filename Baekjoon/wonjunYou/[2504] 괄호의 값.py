import sys

input = sys.stdin.readline

brackets = list(input().rstrip('\n'))

SMALL_LEFT = "("
SMALL_RIGHT = ")"

BIG_LEFT = "["
BIG_RIGHT = "]"

stack = []

tmp = 1
result = 0

for idx in range(len(brackets)):
    if brackets[idx] == SMALL_LEFT:
        tmp *= 2
        stack.append(SMALL_LEFT)

    elif brackets[idx] == BIG_LEFT:
        tmp *= 3
        stack.append(BIG_LEFT)

    elif brackets[idx] == SMALL_RIGHT:
        if not stack or stack[-1] == BIG_LEFT:
            result = 0
            break

        if brackets[idx - 1] == SMALL_LEFT:
            result += tmp
        stack.pop()
        tmp = tmp // 2

    elif brackets[idx] == BIG_RIGHT:
        if not stack or stack[-1] == SMALL_LEFT:
            result = 0
            break

        if brackets[idx - 1] == BIG_LEFT:
            result += tmp

        stack.pop()
        tmp = tmp // 3

if stack:
    result = 0

print(result)