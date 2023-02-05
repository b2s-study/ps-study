
# 풀이 1. 이진탐색 
import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

# 이진탐색을 위한 정렬
n_list.sort()

# m 하나씩 살피기 
for num in m_list:
    
    # 이진탐색 코드
    start = 0
    end = n-1

    # true인지 false인지 
    tf = False

    # start<=end로 해야됨 까먹지 말기 
    while start<=end:
        mid = (start+end)//2

        if num == n_list[mid]:
            # print(mid,'에 데이터가 존재')
            tf = True
            print(1)
            break
        elif num > n_list[mid]:
            start = mid+1
            
        else:
            end = mid-1
            
    if not tf:
        print(0)
        
        
# 풀이 2. 집합으로 풀기

input = sys.stdin.readline
n = int(input())
n_set = set(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))

for num in m_list:				
    print(1) if num in n_set else print(0)	# num이 A 안에 있으면 1, 없으면 0 출력
 