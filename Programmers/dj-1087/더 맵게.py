import sys
import heapq


def solution(scoville, K):
    answer = 0
    min_heap = []
    for s in scoville:
        heapq.heappush(min_heap, s)
    while (True):
        if min_heap[0] >= K:
            break

        if (len(min_heap) == 1) and (min_heap[0] < K):
            answer = -1
            break

        first_food = heapq.heappop(min_heap)
        second_food = heapq.heappop(min_heap)

        new_scoville = first_food + (second_food * 2)
        heapq.heappush(min_heap, new_scoville)
        answer += 1

    return answer
