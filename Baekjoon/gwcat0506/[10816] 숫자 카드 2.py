
# 시간효율 중요 -> count()의 시간 복잡도 O(N)말고 딕셔너리 생성하기 
import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

# 틀린 코드 -> count사용하니 시간초과 
# n_tuple = []
# # n_list 변형 -> [요소개수,요소]의 튜플로 구성하기
# for i in set(n_list):
#     cnt = n_list.count(i)
#     n_tuple.append([i,cnt])
# n_tuple.sort()
# print(n_tuple)

# count 딕셔너리 생성
n_tuple = {}
for i in n_list:
    if i not in n_tuple:
        n_tuple[i] = 1
    else:
        n_tuple[i] +=1
# print(n_tuple)
    
n_list = list(set(n_list))
n_list.sort()
    
result = []
for num in m_list:
    
    # 이진탐색 코드
    start = 0
    end = len(n_list)-1

    # true인지 false인지 
    tf = False

    # start<=end로 해야됨 까먹지 말기 
    while start<=end:
        mid = (start+end)//2

        if num == n_list[mid]:
            tf = True
            result.append(n_tuple[num])
            break
        elif num > n_list[mid]:
            start = mid+1
        else:
            end = mid-1
    if not tf:
        result.append(0)
        continue
    

print(*result)