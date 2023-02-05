# 딕셔너리 이용

import sys

input = sys.stdin.readline
N,X = map(int,input().split())
N_list = list(map(int,input().split()))

print(*[i for i in N_list if i<X])
