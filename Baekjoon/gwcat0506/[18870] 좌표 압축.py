# 딕셔너리 이용

import sys

input = sys.stdin.readline
N = int(input())
N_list = list(map(int,input().split()))
# -10 -9 2 4 4

l = list(set(N_list))
l.sort()

# print('-------')
# print('l',l)

# 딕셔너리 생성
dic = {l[i] : i for i in range(len(l))}
for i in N_list:
    print(dic[i],end=' ')

result = []
# # 이분탐색으로 자기자신을 찾은 후에 그 전까지의 index 출력
# for n in N_list:
#     print('n',n)
    
#     start = 0
#     end = len(l)-1
#     # 이진탐색
#     while start<=end:
#         mid = (start+end)//2
        
#         print(start,end,mid)
#         if l[mid] == n:
#             result.append(mid)
#             print('mid',mid,'n',n)
#             break
#         elif l[mid] > n:
#             start = mid+1
#         else:
#             end = mid-1
#     print(*result)