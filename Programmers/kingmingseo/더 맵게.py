import sys
import heapq
input = sys.stdin.readline

def solution(scoville, k):
    count = 0
    heapq.heapify(scoville)

    while(len(scoville)>0):

        low_hot_food = heapq.heappop(scoville)


        if (low_hot_food < k ):
            new_food = low_hot_food + ((heapq.heappop(scoville)) * 2)
            heapq.heappush(scoville, new_food)
            count = count + 1


        if (len(scoville) == 1 and scoville[0] < k):
            return -1

    return count

