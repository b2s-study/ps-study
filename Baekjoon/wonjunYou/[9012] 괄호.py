import sys

input = sys.stdin.readline

def checkVPS(data) -> bool:
    LEFT_BRACKET = "("
    RIGHT_BRACKET = ")"

    stack = []

    for letter in data:
        if letter == LEFT_BRACKET:
            stack.append(letter)

        elif letter == RIGHT_BRACKET:
            if (stack and stack[-1] == LEFT_BRACKET):
                stack.pop()
                continue

            return False

    if len(stack) == 0:
        return True

    return False

t = int(input().rstrip('\n'))

for _ in range(t):
    data = list(input().rstrip('\n'))

    if checkVPS(data):
        print("YES")
    else:
        print("NO")