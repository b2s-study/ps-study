def solution(sequence, k):
    answer = []

    left, right, length = 0, 0, len(sequence)
    sum_val = sequence[0]

    while left <= right < len(sequence):
        if left > right:
            sum_val = sequence[left]
            right = left
            continue

        if sum_val == k:
            cur_length = right - left + 1
            if length > cur_length:
                length = cur_length
                answer = [left, right]
                print(answer, length)

            sum_val -= sequence[left]
            left += 1

        elif sum_val > k:
            sum_val -= sequence[left]
            left += 1

        elif sum_val < k:
            right += 1
            if right >= len(sequence):
                break
            sum_val += sequence[right]

    return answer
