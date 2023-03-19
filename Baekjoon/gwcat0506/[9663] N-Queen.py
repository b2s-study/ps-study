def check(x): 
    for i in range(x): #인덱스가 행  row[n]값이 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나 대각선이 같으면 false
            return False # 대각선이 같은경우는 두 좌표에서 행 - 행 = 열 - 열 이 같으면 두개는 같은 대각선상에 있다.
    return True
 
def dfs(x):
    global result
 
    if x == N:
        result += 1
    else:
        for i in range(N): 
            row[x] = i
            if check(x): # check가 true이면 계속진행
                dfs(x + 1)
 
N = int(input())
row = [0] * N
result = 0
dfs(0)

print(result)
