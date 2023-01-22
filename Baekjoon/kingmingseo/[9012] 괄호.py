import sys
input = sys.stdin.readline

count = int(input())
temp = []

for j in range (count):
    stack = []
    button = False
    answer = list(input().rstrip())

    for i in answer:

        if i == ')' and len(stack)==0:
            button = True
            break;

        elif i == '(':
            stack.append(i);


        elif i == ')':
            stack.pop();

    if len(stack)!=0:
        temp.append("NO")

    elif button == True:
        temp.append("NO")

    else :
        temp.append("YES")

print(*temp,sep="\n")





