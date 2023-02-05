
# 풀이 1. 시간초과 

import sys
input = sys.stdin.readline

n , m = map(int,input().split())
days = list(map(int,input().split()))

day_sum = []
for i in range(n-m+1):
    day_sum.append(sum(days[i:i+m]))

print(max(day_sum))


# 풀이 2. sum 연산 줄이기 -> 다른 사람 풀이 참고

import sys
input = sys.stdin.readline

n , m = map(int,input().split())
days = list(map(int,input().split()))

day_sum = []
day_sum.append(sum(days[:m]))

for i in range(n - m):
    day_sum.append(day_sum[i] - days[i] + days[m+i])
        
print(max(day_sum))