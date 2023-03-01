import math


def get_candidate_list(knumber: str):
    result = []
    candidate = ""
    for i in range(len(knumber)):
        if knumber[i] == "0":
            if len(candidate) != 0:
                result.append(candidate)
                candidate = ""
            continue
        candidate += knumber[i]

    if len(candidate) != 0:
        result.append(candidate)

    return result


def is_p(candidate):
    candidate = int(candidate)
    if candidate == 1:
        return False
    limit = int(math.sqrt(candidate)) + 1
    for i in range(2, limit):
        if candidate % i == 0:
            return False
    return True


def transfer(n, k):
    result = ""
    while n != 0:
        remain = n % k
        result = str(remain) + result
        n = n // k
    return result


def solution(n, k):
    answer = 0
    knumber = transfer(n, k)
    print(knumber)
    clist = get_candidate_list(knumber)
    print(clist)
    for candidate in clist:
        if is_p(candidate):
            print("p", candidate)
            answer += 1
    return answer
