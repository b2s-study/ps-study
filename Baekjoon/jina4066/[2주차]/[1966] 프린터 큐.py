# 문서의 중요도 큐에 삽입 삭제 연산을 할 때, 마찬가지로 인덱스 큐에도 같은 연산을 수행한다.
# 중요도 큐의 맨 앞 원소가 가장 큰 값이면 출력하고(popleft()), 아니라면 큐의 뒤로 보낸다.
# 출력할 때 마다 카운터 변수를 1씩 증가시키고, 만약 해당 출력 문서의 인덱스가 출력하고자 입력받은 인덱스와 
# 같다면 답을 찾은 것이므로 카운터 값을 화면에 출력한다.

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

# 입력
for _ in range(T):
    n, m = map(int, input().rstrip('\n').split())
    # 문서의 중요도를 담는 큐
    q = deque(list(map(int, input().rstrip('\n').split())))
    # 문서의 인덱스를 담는 큐
    idx = deque(list(range(len(q))))
    target = idx[m]
    
    count = 0
    
    while q:
        if q[0] == max(q): # 중요도 제일 높은 문서 출력
            count += 1
            q.popleft()
            pop_idx = idx.popleft()

            if pop_idx == m:
                print(count)

        else:
            q.append(q.popleft())
            idx.append(idx.popleft())
            
            
        
    

