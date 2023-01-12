import sys

input = sys.stdin.readline

word = input().rsplit('/n')[0].upper()
alphabet_set = set(word)
max_count = 0
count_dict = {}
result = []
for alphabet in alphabet_set:
  alphabet_count = word.count(alphabet)
  max_count = max(max_count, alphabet_count)
  count_dict[alphabet] = alphabet_count

for alphabet in alphabet_set:
  if count_dict[alphabet] == max_count:
    result.append(alphabet)
    
if len(result) > 1:
  print("?")
elif len(result) == 1:
  print(result.pop())
else:
  print("error")