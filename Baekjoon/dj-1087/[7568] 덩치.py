import sys

input = sys.stdin.readline

N = int(input())
score_list = [1] * N
people_info = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  current_person = people_info[i]
  for j in range(i+1, N):
    compare_person = people_info[j]
    if current_person[0] < compare_person[0] and current_person[1] < compare_person[1]:
      score_list[i] += 1
    elif current_person[0] > compare_person[0] and current_person[1] > compare_person[1]:
      score_list[j] += 1
  
print(" ".join(map(str, score_list)))