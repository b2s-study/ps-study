import sys

input = sys.stdin.readline

T = int(input().rstrip('\n'))

for _ in range(T):
    stack = []
    str = input().rstrip('\n')
    
    for j in str:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else:  # 스택에 괄호가 없는 경우 'NO'
                print("NO")
                break
    
    else:  # break 문으로 끊기지 않고 수행되었을 경우
        if not stack:
            print("YES")

        if stack:
            print("NO")
                
    
