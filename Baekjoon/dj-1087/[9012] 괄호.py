import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  brackets = input()
  stack_list = []
  no_error = True

  for b in brackets:
    if len(stack_list) == 0 and b == ")":
      no_error = False
      break
    if b == '(':
      stack_list.append(b)
    elif b == ')':
      stack_list.pop()

  if no_error and len(stack_list) == 0:
    print('YES')
  else:
    print('NO')


