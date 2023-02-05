
# 시간 제한이 0.5초 인 것으로 보아 시간이 중요하다는 것을 나타냄.

import sys
input = sys.stdin.readline

N,S = map(int,input().split())
N_list = list(map(int,input().split()))

N_list.sort()

# 1 2 3 4 5 7 8 9 10
p1 = 0
p2 = 1
ans = sys.maxsize
bubun_sum = 0 

while p1<N and p2<N:

    # 만약 총 합이 S가 넘는다면, p1를 하나씩 옮겨보면서 어디까지 길이가 줄어드나 확인
    if bubun_sum >= S:
        min_length = min(min_length, p2 - p1)
        bubun_sum -= N_list[p1]
        p1 += 1
    elif p2 == N:
        break
    # 만약 총합이 S를 넘지 않는다면, p2 을 오른쪽으로 한칸씩 옮기며 총합이 S를 넘을때까지 더함
    else:
        bubun_sum += N_list[p2]
        p2 += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)