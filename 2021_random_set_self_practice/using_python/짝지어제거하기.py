def solution(s):
    stack = []

    for ch in s:
        if len(stack) == 0 or stack[-1] != ch:
            stack.append(ch)
        else:
            stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0


if __name__ == "__main__":
    print(solution("cdcd"))
