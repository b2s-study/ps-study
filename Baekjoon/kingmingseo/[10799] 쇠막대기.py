import sys
input = sys.stdin.readline

stack = []
stick = list(input().rstrip())
answer = 0

for i in range (0 ,len(stick)):

    if stick[i] == "(":
        stack.append("(")

    else:
        if stick[i-1] == "(":
            stack.pop()
            answer = answer + len(stack)

        else:
            stack.pop()
            answer = answer + 1




print(answer)
