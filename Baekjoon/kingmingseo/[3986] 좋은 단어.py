import sys
input = sys.stdin.readline

count = int(input())
answer = 0


for i in range(count):
    temp = []
    stack = list(input().rstrip())

    for j in stack:
        if len(temp)==0:
            temp.append(j)

        elif j == temp[-1]:
            temp.pop()

        else :
            temp.append(j)


    if len(temp)==0:
        answer = answer +1

print(answer)




