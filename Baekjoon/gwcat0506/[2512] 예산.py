
# 몰라서 답지 참고함. 
import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

N_list.sort()

# 이진탐색하기 
start = 0
end = N_list[-1]

while start<=end:
    mid = (start+end)//2
    # print(start,end,mid)
    
    target = 0
    for n in N_list:
        if n < mid:
            target += n
        else:
            target += mid
    
    
    if target > M:
        end = mid - 1
    else:
        start = mid +1
    
print(end)
