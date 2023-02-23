import sys

input = sys.stdin.readline

N = int(input().rstrip('\n'))
count = 0

for _ in range(N):
    stack = []
    s = input().rstrip('\n')

    for i in range(len(s)):
        if stack: # 스택 내에 값이 있을 때
            if s[i] == stack[-1]:
                stack.pop()
            
            else:
                stack.append(s[i])

        else: # 스택 내에 값이 없을 때
            stack.append(s[i])

    if not stack:
        count += 1

print(count)



    