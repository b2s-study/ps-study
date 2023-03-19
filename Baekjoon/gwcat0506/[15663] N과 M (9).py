import sys

input = sys.stdin.readline

n,m = list(map(int,input().split()))
n_list = sorted(list(map(int,input().split())))
visited = [0]*n

s = []

def dfs():
    
    if len(s)==m:
        print(*s)
        return 
    idx = -1
    for i in range(n):
        if visited[i]==0 and idx != n_list[i]:
            visited[i] = 1 # 방문처리
            
            s.append(n_list[i])
            idx = n_list[i]
            dfs()  
            visited[i] = 0 # 초기화
            s.pop()  

dfs()