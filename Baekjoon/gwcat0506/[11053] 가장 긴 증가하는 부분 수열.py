
import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))

dp = [1]*N

for i in range(1,N):
    for j in range(i):
        if N_list[i] > N_list[j]:
            dp[i] = max(dp[i],dp[j]+1)
            
print(max(dp))
