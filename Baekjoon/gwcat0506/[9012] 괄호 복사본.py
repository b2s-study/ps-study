# https://www.acmicpc.net/problem/9012
# 괄호



# 풀이1. 너무 어렵게 구현했당 !!!
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    st = []
    
    N_list = list(map(str,sys.stdin.readline()))

    # 첫 행은 어차피 '(' 이므로 넣어주기, ')'이면 어차피 괄호가 완성이 안 되므로 바로 stop
    if N_list[0] == ')':
        print('NO')
        pass
    else:
        st.append(N_list[0])
    # print('st',st) 
    
    for i in range(1,len(N_list)):
        # '(' 면 push(append)
        if N_list[i] == "(":
            st.append(N_list[i])
        if N_list[i] == ')':
            if len(st)!=0:
                if st[-1]== '(' :
                    st.pop()
                else:
                    print('NO')
                    break
            else:
                st.append(N_list[i])
                break

        print('st',st) 
    # stack이 모두 비었을 경우 -> 올바른 괄호 문자열
    if len(st)==0:
        print('YES')
    else:
        print('NO')
    

# 풀이2. 다시 간단화 시키기 -> 문제점 -> break를 한 후에도 나머지 것들을 실행시켜야 한다...

import sys
N = int(sys.stdin.readline())

for _ in range(N):
    st = []
    N_list = list(map(str,sys.stdin.readline()))
    
    for i in N_list:
        if len(st)==0 and i==')':
            print('NO')
            break
        if i == '(':
            st.append(i)
        # ')'일 때 
        elif st[-1]=='(':
            st.pop()
        else:
            print('NO')
            break
    if len(st)==0:
        print('YES')
    else:
        print('NO')
            
            
# 풀이 3. 함수화 시키기 

#stack 이용한 () 문제

import sys


def check(string):

    stack = []
    for i in string:
        if len(stack) == 0 and i ==')':
            return 'NO'
        if i == '(':
            stack.append(i)
        elif stack[-1]=='(':
            stack.pop()
        else:
            return 'NO'
    if len(stack)==0:
        return 'YES'
    return 'NO'



input = sys.stdin.readline
n = int(input().strip())
for i in range(n):
    string = input().strip()
    print(check(string))