

# 아예 모르겠다. 정답 확인해서 품...
# 이진탐색 문제 중 가장 어렵게 느껴짐.

import sys
input = sys.stdin.readline

n , c = map(int,input().split())

arr = [int(input()) for _ in range(n)]

# 이진 탐색을 위한 sort
arr.sort()

start = 1
# 거리의 최댓값
end = arr[-1]+arr[0]
ans = 0

while start<=end:
    mid = (start+end)//2
    count = 1
    current = arr[0]
    
    for i in range(1,n):
        if current + mid <= arr[i]:
            current = arr[i]
            count+=1
    if count >= c:
        # 사이 거리 넓히기 
        start = mid+1
        ans = mid
    else:
        # 좁히기
        end = mid-1
print(ans)
                    # 