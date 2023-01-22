
import math


def solution(progresses, speeds):
    day_list = []
    for speed, progress in zip(speeds, progresses):
        day = math.ceil((100 - progress) / speed)
        # print(speed,progress,day)
        day_list.append(day)

    # day_list =  [7,3,9]

    day_list.reverse()

    result = []
    # #     9,3,7
    st = []
    for i in range(len(day_list)):
        if st and (st[-1] > day_list[i]):
            result.append(len(st))

            # stack초기화 & st.append(day_list[i])

    return result

print(solution([90,95,99],[1,1,1]))