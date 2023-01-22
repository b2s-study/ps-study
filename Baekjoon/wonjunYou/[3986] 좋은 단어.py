import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

result = 0

for _ in range(n):
    word = list(input().rstrip('\n'))

    stack = []

    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)

    if not stack:
        result += 1

print(result)