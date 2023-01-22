import sys

input = sys.stdin.readline

S = input().rstrip('\n')
left, right = 0, 0

sub_words = []

for length in range(0, len(S)):
    for idx in range(len(S) - length):
        left = idx
        right = idx + length

        sub_words.append(S[left : right + 1])

print(len(set(sub_words)))