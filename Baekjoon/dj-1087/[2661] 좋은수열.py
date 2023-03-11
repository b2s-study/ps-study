import sys

# 반복문으로 이전에 겹치는 경우가 있는 지 끝까지 확인


def is_valid(case, sequence):
    if len(sequence) == 0:
        return True

    check_list = sequence + [case]
    for check_length in range(1, len(check_list) // 2 + 1):
        a = check_list[len(check_list) - check_length:]
        b = check_list[len(check_list) - 2 *
                       check_length: len(check_list) - check_length]
        if a == b:
            return False
    return True


def dfs(sequence):
    global N
    if len(sequence) == N:
        return sequence

    for i in range(1, 4):
        if is_valid(i, sequence):
            sequence.append(i)
            result = dfs(sequence)
            if len(result) != 0:
                return result
            sequence.pop()
    return []


input = sys.stdin.readline

N = int(input())
sequence = dfs([])
for s in sequence:
    print(s, end="")
