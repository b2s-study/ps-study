
import sys

N = int(sys.stdin.readline())

dp = [0]*N

dp[0]=1
dp[1]=1

for i in range(2,N):
    
    dp[i] = dp[i-1]+dp[i-2]
    
print(dp[N-1])
