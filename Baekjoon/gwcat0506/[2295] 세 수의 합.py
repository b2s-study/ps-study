
# # 조합 풀이 
# import sys
# from itertools import combinations, permutations

# input = sys.stdin.readline

# n = int(input())

# n_list = []
# for _ in range(n):
#     u = int(input())
#     n_list.append(u)

# # n_list = [1,2,3,5,6,10,18]
# n_list.sort()

# combis = list(combinations(n_list, 3))

# l = []
# for combi in combis:
#     a,b,c = combi
#     l.append(a+b+c)

# # print(combis)
# # 조합의 합을 l에 append한다. 
# l.sort()
# # print(l)

# import heapq
# # result를 heap으로 구성
# heap=[]
# # 정렬 후 이진탐색 하기 
# for x in n_list[3:]:
#     # x가 l에 있는지 확인
#     start = 0
#     end = len(l)-1
    
#     while start<=end:
#         mid = (start+end)//2
        
#         if l[mid]==x:
#             # 최대 힙
#             heapq.heappush(heap,[-x,x])
#             break
#         elif l[mid] < x:
#             start = mid+1
#         else:
#             end = mid -1

# print(heapq.heappop(heap)[1])
        
    

# 조합 풀이2 
import sys
from itertools import combinations, permutations

input = sys.stdin.readline

n = int(input())

n_list = []
for _ in range(n):
    u = int(input())
    n_list.append(u)

# n_list = [1,2,3,5,6,10,18]
n_list.sort()


import heapq
# result를 heap으로 구성
heap=[]
# 정렬 후 이진탐색 하기 
for x in range(3,len(n_list)):
    l = []
    combis = list(combinations(n_list[:x], 3))
    for combi in combis:
        l.append(sum(combi))
    
    l.sort()
    # print('l',l)
    
    # x가 l에 있는지 확인
    start = 0
    end = len(l)-1
    
    while start<=end:
        mid = (start+end)//2
        
        if l[mid]==n_list[x]:
            # 최대 힙
            heapq.heappush(heap,[-n_list[x],n_list[x]])
            break
        elif l[mid] < n_list[x]:
            start = mid+1
        else:
            end = mid -1

# print(heap)
print(heapq.heappop(heap)[1])

