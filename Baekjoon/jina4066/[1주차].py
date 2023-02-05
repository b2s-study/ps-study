# 1
# year = int(input())

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#   print(1)
# else:
#   print(0)

#2
# H, M= map(int, input().split())

# if (H == 0): 
#   if (M >= 45):
#     M -= 45
#   else:
#     H = 23
#     M += 15
# else:
#   if (M >= 45):
#     M -= 45
#   else:
#     H -= 1
#     M += 15

# print(H, M)

#3 
# a = int(input())

# sum = 0

# for i in range(a+1):
#   sum += i

# print(sum)

#4
# import sys
# T = int(input())
# list = []

# for i in range(T):
#   A, B = map(int, sys.stdin.readline().strip().split())
#   list.append(A+B)

# for i in range(T):
#   print(list[i])

#5
# N = int(input())

# for i in range(N):
#   print("*" * (i+1))

#6
# N = int(input())

# for i in range(N):
#   print(" " * (N - (i + 1)) + "*" * (i + 1))

#10818
# N = int(input())
# str = list(map(int, input().split()))

# min = str[0]
# max = str[0]

# for i in range(N):
#   if min > str[i]:
#     min = str[i]
#   if max < str[i]:
#     max = str[i]

# print(min, max)

#3052
# remainList = []

# for i in range(10):
#   x = int(input())
#   if ((x % 42) not in remainList):
#     remainList.append(x % 42)

# print(len(remainList))

#[11720]
# N = int(input())
# numList = list(map(int, input()))

# sum = 0

# for i in range(N):
#   sum += numList[i]

# print(sum)

#[1157] 단어 공부
# import sys

# input = sys.stdin.readline

# word = input().strip().upper()

# #중복값을 제거한 알파벳들을 word_list에 넣어준다
# word_list = list(set(word))
# cnt = []

# # word에서 각 알파벳들의 개수를 센 후 cnt 리스트에 추가한다. 
# # word_list에는 알파벳이, cnt 리스트에는 그 알파벳에 대응하는 카운트 수가 삽입된다. 
# for i in word_list:
#     count = word.count(i)
#     cnt.append(count) 

# # 만약 cnt 리스트에서의 max값이 cnt 리스트 안에서 2번 이상 카운트 되어지면 "?" 출력
# if cnt.count(max(cnt)) >= 2:
#     print("?")

# else:
#     print(word_list[(cnt.index(max(cnt)))])

#[1152] 단어의 개수

    









