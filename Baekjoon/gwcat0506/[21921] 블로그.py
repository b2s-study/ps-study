

import sys
input = sys.stdin.readline

n , m = map(int,input().split())
days = list(map(int,input().split()))

if max(days)==0:
    print("SAD")
    
else:

    day_sum = []
    day_sum.append(sum(days[:m]))
    
    max_s = sum(days[:m])
    cnt = 1

    for i in range(n - m):
        s = day_sum[i] - days[i] + days[m+i]
        day_sum.append(s)
        
        if max_s<s:
            max_s = s
            cnt=1
        elif max_s == s:
            cnt+=1
        
    print(max_s)
    print(cnt)