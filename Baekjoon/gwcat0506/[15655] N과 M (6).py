import sys

input = sys.stdin.readline

n,m = list(map(int,input().split()))
n_list = list(map(int,input().split()))
n_list.sort()

s = []
def dfs(start):
    
    if len(s)==m:
        print(" ".join(map(str,s)))
        return 
    
    for i in range(start,n):
        s.append(n_list[i])
        dfs(i+1)
        s.pop()
        
    
dfs(0)