import sys

input = sys.stdin.readline

string = input().rstrip()

sub_string_set = set()
for i in range(0, len(string)):
  for j in range(0, len(string)):
    sub_string_set.add(string[i:j+1])

sub_string_set.remove("")
print(len(sub_string_set))
    