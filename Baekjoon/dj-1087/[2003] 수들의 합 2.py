import sys

N, M = map(int, input().split())
A = list(map(int, input().split()))

left, right = 0, 0
current_sum = A[0]
case_count = 0
while (True):
    if (left > right) or (right >= len(A)):
        break

    # print("left+1, right+1", left+1, right+1)
    if current_sum < M:
        right += 1
        if right >= len(A):
            break

        current_sum += A[right]

    elif current_sum > M:
        current_sum -= A[left]
        left += 1
        if (current_sum == 0) and (left < len(A)):
            current_sum += A[left]
            right += 1

    else:
        # print("left+1, right+1", left+1, right+1)

        case_count += 1
        current_sum -= A[left]
        left += 1
        right += 1
        if right >= len(A):
            break
        current_sum += A[right]

print(case_count)
