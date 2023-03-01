import heapq


def solution(n, info):
    answer = [0] * 11
    info.reverse()
    info = list(enumerate(info))  # element: (점수, 화살 수)
    pq = []
    for each in info:
        score, arrows = each
        heapq.heappush(pq, (arrows, -1*score, score))

    rion = []
    while pq:
        arrows, _, score = heapq.heappop(pq)
        if n >= arrows+1:
            heapq.heappush(rion, (score, arrows+1))
            n -= (arrows+1)
        else:
            if rion[0][0] > score:
                continue
            elif rion[0][0] == score and rion[0][1] <= (arrows+1):
                continue
            n = n + rion[0][1]
            heapq.heappop(rion)
            heapq.heappush(rion, (score, arrows+1))
            n = n - (arrows+1)

        for score, arrows in rion:
            answer[score] = arrows

        answer.reverse()
    return answer
