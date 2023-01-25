# https://www.acmicpc.net/problem/10799

# stack이용
import sys

# 문자열을 한 번에 받을 때 strip() 필수 ! 
s_list = list(map(str, sys.stdin.readline().strip()))
# print(s_list)

st = []
result = 0

for i in range(len(s_list)):
    
    # push
    if s_list[i] == '(':
        st.append(s_list[i])
    
    # pop
    elif s_list[i-1]=='(':
            st.pop()
            # stack에 있는 요소만큼 더해준다 !(key point)
            result += len(st)
    else:       
        # ) 다음 ) 일 경우 stack에 pop하고 result에 1 증가 
        st.pop() 
        result += 1 #끄트머리 막대기 부분을 더해준다
        
        
print(result)