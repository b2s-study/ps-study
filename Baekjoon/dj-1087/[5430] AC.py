import sys
from collections import deque


def to_string(number_deque):
    if len(number_deque) == 0:
        return "[]"
    result = "["
    for number in number_deque:
        result += str(number)+','
    result = result[: -1] + "]"
    return result


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    number_input = input().rstrip()
    number_deque = deque(number_input[1: -1].split(','))
    if number_input[1: -1] == '':
        number_deque.clear()

    head_start_left = True
    occured_error = False
    for function_name in p:
        if function_name == 'R':
            head_start_left = not head_start_left
        elif function_name == 'D':
            if len(number_deque) == 0:
                occured_error = True
                break
            if head_start_left:
                number_deque.popleft()
            else:
                number_deque.pop()

    if occured_error:
        print("error")
        continue

    if not head_start_left:
        number_deque.reverse()
    print(to_string(number_deque))
