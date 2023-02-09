import sys

input = sys.stdin.readline

word = input().strip().upper()

#중복값을 제거한 알파벳들을 word_list에 넣어준다
word_list = list(set(word))
cnt = []

# word에서 각 알파벳들의 개수를 센 후 cnt 리스트에 추가한다. 
# word_list에는 알파벳이, cnt 리스트에는 그 알파벳에 대응하는 카운트 수가 삽입된다. 
for i in word_list:
    count = word.count(i)
    cnt.append(count) 

# 만약 cnt 리스트에서의 max값이 cnt 리스트 안에서 2번 이상 카운트 되어지면 "?" 출력
if cnt.count(max(cnt)) >= 2:
    print("?")

else:
    print(word_list[(cnt.index(max(cnt)))])

