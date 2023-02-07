def solution(queue1, queue2):
    start = 0
    end = len(queue1) - 1

    new_queue = queue1 + queue2

    L = sum(queue1)
    R = sum(queue2)

    count = 0
    for _ in range(2 * len(new_queue)):
        if (L == R):
            return count

        if (L > R):
            L -= new_queue[start]
            R += new_queue[start]
            start = (start + 1) % len(new_queue)

        elif (L < R):
            end = (end + 1) % len(new_queue)
            L += new_queue[end]
            R -= new_queue[end]

        count += 1

    return -1