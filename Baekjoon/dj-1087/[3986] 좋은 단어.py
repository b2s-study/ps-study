import sys

input = sys.stdin.readline

N = int(input())
good_word_count = 0
for _ in range(N):
    word = input().rstrip()
    stack = []

    for current_alphabet in word:
        if len(stack) == 0:
            stack.append(current_alphabet)
            continue

        if current_alphabet == stack[-1]:
            stack.pop()
        else:
            stack.append(current_alphabet)

    if len(stack) == 0:
        good_word_count += 1

print(good_word_count)
