import sys

input = sys.stdin.readline

n,m = list(map(int,input().split()))
n_list = list(map(int,input().split()))
n_list.sort()

s = []
def dfs():
    
    if len(s)==m:
        print(" ".join(map(str,s)))
        return 
    
    for i in range(n):
        s.append(n_list[i])
        dfs()
        s.pop()
        
    
dfs()