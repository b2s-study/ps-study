import sys

input = sys.stdin.readline

test_case = input().rstrip()

result = 0
stack = []
prev = ''
for i in range(len(test_case)):
    if i == 0:
        stack.append(test_case[i])
        prev = test_case[i]
        continue

    current = test_case[i]
    # 레이저인 경우
    if prev == '(' and current == ')':
        stack.pop()
        result += len(stack)
        prev = ''

    elif current == ')':
        stack.pop()
        result += 1

    elif current == '(':
        stack.append(current)

    prev = current

print(result)
