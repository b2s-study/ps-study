import heapq

def solution(scoville, K):
    q = []

    for value in scoville:
        heapq.heappush(q, value)

    cnt = 0

    while True:
        if len(q) == 1:
            if q[0] < K:
                return -1
            else:
                return cnt

        if q[0] >= K:
            return cnt

        first = heapq.heappop(q)
        second = heapq.heappop(q)

        heapq.heappush(q, (first + (second * 2)))

        cnt += 1