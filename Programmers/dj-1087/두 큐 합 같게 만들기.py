from collections import deque


def solution(queue1, queue2):
    # - 덱 이용 방식 (최적화)
    answer = 0
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    target_sum = (sum(queue1) + sum(queue2)) / 2
    if target_sum != int(target_sum):
        return -1

    current_sum = sum(deque1)
    current_length = len(deque1)
    total_length = len(deque1) + len(deque2)
    head_index = 0
    while (True):
        if (current_length == 0) or (current_length == total_length) or (head_index >= total_length):
            answer = -1
            break

        if current_sum < target_sum:
            value = deque2.popleft()
            deque1.append(value)
            current_sum += value
            current_length += 1
        elif current_sum > target_sum:
            value = deque1.popleft()
            deque2.append(value)
            current_sum -= value
            current_length -= 1
            head_index += 1
        else:
            break

        answer += 1

    return answer


# def solution(queue1, queue2):
#     # - 덱 이용 방식
#     answer = 0
#     deque1 = deque(queue1)
#     deque2 = deque(queue2)
#     target_sum = (sum(queue1) + sum(queue2)) / 2
#     if target_sum != int(target_sum):
#         return -1

#     head_index = 0
#     while (True):
#         if (len(deque1) == 0) or (len(deque1) == len(deque1) + len(deque2)) or (head_index >= len(deque1) + len(deque2)):
#             answer = -1
#             break

#         current_sum = sum(deque1)
#         if current_sum < target_sum:
#             value = deque2.popleft()
#             deque1.append(value)
#         elif current_sum > target_sum:
#             value = deque1.popleft()
#             deque2.append(value)
#             head_index += 1
#         else:
#             break

#         answer += 1

#     return answer


# def solution(queue1, queue2):
#     # - 투 포인터 방식
#     answer = 0
#     half_length = len(queue1)
#     left, right = 0, half_length
#     queue1.extend(queue2)
#     target_sum = sum(queue1) / 2
#     if target_sum != int(target_sum):
#         return -1

#     while (True):
#         current_sum = sum(queue1[left:right])
#         if current_sum < target_sum:
#             right += 1
#         elif current_sum > target_sum:
#             left += 1
#         else:
#             break

#         answer += 1

#         if right > len(queue1):
#             answer = -1
#             break

#     return answer
