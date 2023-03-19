

# 이전에 풀었던 코드
from itertools import permutations
import sys
 
# 주어진 값 입력
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
 
# permutation 저장(per: reference of permutation tuples)
per = permutations(nums)
maximum = 0
# print(list(per))

# 순열마다 차이를 더해(s), maximum 보다 크면 maximum를 update
for i in per:
    total = 0
    for j in range(len(i)-1):
        total += abs(i[j]-i[j+1])
    maximum = max(total,maximum)
 
print(maximum)