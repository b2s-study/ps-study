#enumerate 개념 처음 사용

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip('\n'))
q = deque(enumerate(map(int, input().rstrip('\n').split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(*ans)



    # for i in range(len(q)):
    #     if idx[i] == q[0]:
    #         count.append(i+1)
    

    # q.popleft()
    # q.rotate(-(q[0] - 1))
    

    

    