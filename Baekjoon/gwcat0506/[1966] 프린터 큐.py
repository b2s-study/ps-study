# https://www.acmicpc.net/problem/1966


import sys

T = int(sys.stdin.readline())


for _ in range(T):

    
    n, m = list(map(int,sys.stdin.readline().split(" ")) ) 
    imp = list(map(int,sys.stdin.readline().split(" ")) ) 
    idx = list(range(len(imp)))

    idx[m] = 'target'
    
