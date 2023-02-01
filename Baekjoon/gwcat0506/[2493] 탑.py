import sys

input = sys.stdin.readline
N = int(input())
N_list = list(map(int,input().split()))

st = []
result = []

for i in range(0,N):
    while st:
        if N_list[st[-1]] >= N_list[i] :
            # 9 < 5
            break
        else:
            st.pop()   
    if st:
        result.append(st[-1]+1)
    else:
        result.append(0)
    st.append(i)

# print(st)
print(*result)