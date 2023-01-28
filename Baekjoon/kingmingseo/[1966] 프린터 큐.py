import sys
from collections import deque
input = sys.stdin.readline


testcase= int(input())

for i in range (testcase):
    printnum , order = map(int,input().split())
    priority = list(map(int,input().split()))
    priority_deq =deque()
    num = 0

    for i in priority:
        priority_deq.append(i)

    priority.sort()

    while(True):
        max_num = max(priority)

        if order == 0 and max_num != priority_deq[0]:   #타겟이 첫 위치에 왔는데 최대값이 아닌 경우
            priority_deq.rotate(-1)
            order = len(priority)-1

        elif order !=0 and max_num == priority_deq[0]: #첫 위치에 온것이 타겟이 아닌데 최대 값인 경우
            priority_deq.popleft()
            del priority[len(priority)-1]
            order = order -1
            num = num + 1

        elif order!=0 and max_num != priority_deq[0]: #첫 위치에 온것이 타겟도 아니고 최대값도 아닌경우
            priority_deq.rotate(-1)
            order = order - 1

        elif order==0 and max_num == priority_deq[0]: #첫 위치에 온것이 타겟이면서 최대값인 경우
            print(num + 1)
            break
















