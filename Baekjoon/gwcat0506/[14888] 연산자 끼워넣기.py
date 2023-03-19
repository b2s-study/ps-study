# 뭐가 틀린거죠

import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
plus, minus, mul, div = map(int,input().split())


# 값 초기화 
minimum = 1e9
maximum = -1e9


def dfs(depth,total):
    global minimum, maximum, plus, minus, mul, div
    
    # return 조건
    # 숫자를 n개 만큼 모두 사용했을 때
    if depth == n:
        minimum = min(total, minimum)
        maximum = max(total, maximum)
        return 
    
    # print(total,minimum,maximum)
    if plus > 0:
        plus-=1
        total+=nums[depth]
        dfs(depth+1,total)
        plus+=1
        
    if minus > 0:
        minus-=1
        total-=nums[depth]
        dfs(depth+1,total)
        minus+=1
        
    if mul > 0:
        mul-=1
        total*=nums[depth]
        dfs(depth+1,total)
        mul+=1
        
    if div > 0:
        div-=1
        total = total//nums[depth]
        dfs(depth+1,total)
        div+=1
        
    
# 처음에 깊이 1부터 탐색  
dfs(1,nums[0])
print(maximum)
print(minimum)