# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 몇개만 통과됨..
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return -> 이걸 어떻게 처리할지..
import heapq

heap = []
def solution(scoville, K):

#     scoville을 힙으로 만들어 준다. 
    for sco in scoville:
        heapq.heappush(heap,sco)
    
    result = 0
    while heap[0] < K:
#             스코빌을 합쳐 다시 push 한다.
        heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        result+=1
        # print(heap)
        
    return result

