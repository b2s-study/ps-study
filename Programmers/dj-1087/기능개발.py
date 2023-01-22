def solution(progresses, speeds):
    answer = []
    required_days_list = []
    for i in range(len(progresses)):
        calculated_days = (100 - progresses[i]) / speeds[i]
        required_days = 0
        if int(calculated_days) == calculated_days:
            required_days = int(calculated_days)
        else:
            required_days = int(calculated_days) + 1

        if i == 0 or len(required_days_list) == 0:
            required_days_list.append(required_days)
            continue

        if required_days > required_days_list[-1]:
            answer.append(len(required_days_list))
            required_days_list = [required_days]
        else:
            required_days_list.append(required_days)

    if len(required_days_list) > 0:
        answer.append(len(required_days_list))

    return answer


N = int(input())

for _ in range(N):
    progresses = list(map(int, input()[1:-1].split(",")))
    speeds = list(map(int, input()[1:-1].split(",")))

    answer = solution(progresses, speeds)
    print(answer)
