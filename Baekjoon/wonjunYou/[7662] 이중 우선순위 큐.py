import sys, heapq

input = sys.stdin.readline

def synchronize(heap):
    while heap and not check[heap[0][1]]:
        heapq.heappop(heap)

T = int(input().rstrip('\n'))

for _ in range(T):
    maxHeap = []
    minHeap = []
    k = int(input().rstrip('\n'))

    check = [0] * k

    for i in range(k):
        opr, num = input().rstrip('\n').split()

        if opr == "I":
            heapq.heappush(minHeap, (int(num), i))
            heapq.heappush(maxHeap, (-1 * int(num), i))
            check[i] = 1

        elif opr == "D":
            if num == "1":
                synchronize(maxHeap)
                
                if maxHeap:
                    check[heapq.heappop(maxHeap)[1]] = 0

            elif num == "-1":
                synchronize(minHeap)
                
                if minHeap:
                    check[heapq.heappop(minHeap)[1]] = 0
                    
    synchronize(maxHeap)
    synchronize(minHeap)

    if maxHeap and minHeap:
        print(-1 * maxHeap[0][0], minHeap[0][0])

    else:
        print('EMPTY')