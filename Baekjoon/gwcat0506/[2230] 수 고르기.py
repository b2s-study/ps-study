

import sys
input = sys.stdin.readline
N,M = map(int,input().split())
N_list = [int(input().strip()) for _ in range(N)]

N_list.sort()

p1 = 0
p2 = 1
# ans = N_list[-1]
# 이것 때문에 틀렸다구?? -> sys.maxsize 꼭 써줘야 함... 참고로 정수의 최대 사이즈를 나타냄.
ans = sys.maxsize

while p1<N and p2<N:
    # print(p1,p2)
    diff = N_list[p2] - N_list[p1]
    if diff == M:
        ans = M
        break
    elif  diff > M:
        # print(M)
        ans = min(ans,diff)
        p1+=1
    
    else:
        p2+=1
print(ans)
        