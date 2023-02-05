import sys

A = int(sys.stdin.readline())
A_list = list(map(int,sys.stdin.readline().split()))

dp = [1]*A
a = 0
for i in range(1,A):
    for j in range(i):
        if A_list[i] > A_list[j]:
            dp[i] = max(dp[i],dp[j]+1)
            
        if A_list[i] < A_list[j]:
            # if 
        # 모르겠어요..
# print(max(dp))
