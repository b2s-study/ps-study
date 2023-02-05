
import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))

# 이진 탐색을 위한 sort
N_list.sort()

start = N_list[0]
end = N_list[-1]*2
 
 
# 모르겠다.... ㅠㅠ