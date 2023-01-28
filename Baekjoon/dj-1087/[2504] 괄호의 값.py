import sys


def is_opened_bracket(current_bracket):
    return current_bracket == '(' or current_bracket == '['


def is_pair(current_bracket, stack_pop):
    if current_bracket == ')':
        return stack_pop == '('
    elif current_bracket == ']':
        return stack_pop == '['


def get_score(brackets):
    if brackets[0] == "(" and brackets[1] == ")":
        return 2
    elif brackets[0] == "[" and brackets[1] == "]":
        return 3
    else:
        return 0


def is_small_pair(bracket):
    return bracket == '('


def calculate(brackets):
    if len(brackets) == 0:
        return 1
    if len(brackets) == 2:
        return get_score(brackets)

    stack = []
    i = 0
    while (True):
        if i >= len(brackets):
            break

        current_bracket = brackets[i]
        if is_opened_bracket(current_bracket):
            stack.append(current_bracket)
        elif is_pair(current_bracket, stack[-1]):
            stack.pop()
            if len(stack) == 0:
                multiply_number = 2 if is_small_pair(brackets[0]) else 3
                if (i >= len(brackets) - 1):
                    return multiply_number * calculate(brackets[1:i])
                return multiply_number * calculate(brackets[1:i]) + calculate(brackets[i+1:])
        i += 1

    if len(stack) > 0:
        raise Exception()


input = sys.stdin.readline

brackets = input().rstrip()
result = 0
try:
    result = calculate(brackets)
except Exception as e:
    result = 0

print(result)
