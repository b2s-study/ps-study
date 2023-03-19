import sys

input = sys.stdin.readline

n,m = list(map(int,input().split()))
n_list = sorted(list(map(int,input().split())))
visited = [0]*len(n_list)

s = []

def dfs(start):
    
    if len(s)==m:
        print(*s)
        return 
    idx = -1
    for i in range(start,len(n_list)):
        if visited[i]==0 and idx != n_list[i]:
            visited[i] = 1 # 방문처리
            
            s.append(n_list[i])
            idx = n_list[i]
            dfs(i+1)  
            visited[i] = 0 # 초기화
            s.pop()  

dfs(0)