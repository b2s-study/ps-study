import sys
import heapq
input = sys.stdin.readline
test_case = int(input())

def mid(data):
    left_heap = []
    right_heap = []
    answer = []
    k = 1
    for i in data:

        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -i)

        else:
            heapq.heappush(right_heap, i)

        if right_heap and -left_heap[0] > right_heap[0]:
            left_temp = heapq.heappop(left_heap)
            right_temp = heapq.heappop(right_heap)
            heapq.heappush(right_heap, -left_temp)
            heapq.heappush(left_heap, -right_temp)

        if k % 2 == 1:
            answer.append(-left_heap[0])

        k = k+1

    print(len(answer))
    for j in answer:
        print(j, end = ' ')






for i in range(test_case):
    temp = []
    N = int(input())
    if N>=10:
        for j in range (N//10+1):
            temp = temp + list(map(int,input().split()))
    else:
        temp = temp + list(map(int, input().split()))

    mid(temp)
    print()



