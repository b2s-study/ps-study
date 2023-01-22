from collections import deque
def solution(progresses, speeds):
    idx = 0
    cnt = 0
    res = []

    while (idx < len(progresses)):
        if progresses[idx] >= 100:
            cnt += 1
            idx += 1
            continue

        if cnt > 0:
            res.append(cnt)
            cnt = 0

        for i in range(idx, len(progresses)):
            progresses[i] += speeds[i]

    res.append(cnt)

    return res