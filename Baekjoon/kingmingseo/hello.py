import math


def solution(progresses, speeds):
    temp = []
    temp2 = []
    answer = [0]

    for i in progresses:
        temp.append(100 - i)

    for j in range(len(progresses)):
        temp2.append(math.ceil(temp[j] / speeds[j]))

    max2 = temp2[0]
    for x in range (len(temp2)):
        if(temp2[x] > max2):
            max2 = temp2[x]
            answer.append(1)
        else:
            answer[-1]=answer[-1]+1

    return answer


