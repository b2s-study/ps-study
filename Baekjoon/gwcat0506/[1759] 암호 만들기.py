import sys

input = sys.stdin.readline

def dfs(depth,start):
    
    if depth == l:
        
        # 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음 확인
        # 모음 자음
        mo, ja = 0, 0

        for j in range(l):
            if password[j] in 'aeiou':
                mo += 1
            else:
                ja += 1

        # 모음 1개 이상, 자음 2개 이상
        if mo >= 1 and ja >= 2:
            print("".join(password))

        return 
    
    for i in range(start,c):
        password.append(strings[i])
        dfs(depth+1,i+1)
        password.pop()

l,c = map(int,input().split())
strings = sorted(list(map(str,input().split())))

password = []
dfs(0,0)
