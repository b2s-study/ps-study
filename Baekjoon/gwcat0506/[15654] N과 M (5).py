

n,m = list(map(int,input().split()))

n_list = list(map(int,input().split()))
n_list.sort()

s = []

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in n_list:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
    
dfs()