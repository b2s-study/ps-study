import sys

input = sys.stdin.readline

n,m = list(map(int,input().split()))
n_list = sorted(list(set(map(int,input().split()))))

s = []

def dfs(start):
    
    if len(s)==m:
        print(*s)
        return 
    
    for i in range(start,len(n_list)):
        s.append(n_list[i])
        dfs(i)  
        s.pop()  

dfs(0)