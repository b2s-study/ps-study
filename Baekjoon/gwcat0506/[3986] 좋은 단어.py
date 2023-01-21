# https://www.acmicpc.net/problem/3986

# stack을 활용
import sys

n = int(sys.stdin.readline())
res = 0

# 단어의 수만큼 반복하면 단어를 확인
for _ in range(n):

    # strip()을 이용해서 빈칸(\n) 삭제
    s_list = list(map(str, sys.stdin.readline().strip()))
    
    # stack 생성
    st = []

    for i in s_list:
        # 스택이 빈칸이 아니고, 
        # 스택의 마지막 요소와 현재 탐색하고 있는 요소와 같으면 pop
        if st and st[-1] == i:
            st.pop()
            
        # 아니면 push
        else:
            st.append(i)

    # 스택이 모두 pop 됐다면 좋은 단어 ! 
    if len(st) == 0:
        res+=1

print(res)