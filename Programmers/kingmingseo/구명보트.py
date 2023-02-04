import sys
input = sys.stdin.readline

def solution(people, limit):
    people.sort()

    start = 0
    end = len(people) - 1
    answer = 0
    temp = 0
    while(start <= end):

        value = people[start] + people[end]
        if start == end and people[start] <= limit :
            answer = answer +1
            break
        elif value <= limit:
            start = start + 1
            end = end -1
            answer = answer + 1

        else :
            end = end - 1
            answer = answer + 1


    if answer == 0 :
        return 1





    return answer





