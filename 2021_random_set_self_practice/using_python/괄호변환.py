def split_paren(p):
    cnt_left = 0
    cnt_right = 0
    stack = []
    for i, ch in enumerate(p):
        stack.append(ch)
        if ch == '(':
            cnt_left += 1
        else:
            cnt_right += 1
        if cnt_left == cnt_right and cnt_left != 0:
            return ''.join(stack), p[i + 1:]
    return -1


def is_right(paren):
    stack = []
    for ch in paren:
        if ch == '(':
            stack.append('(')
        elif ch == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return stack == []


def reverse_paren(txt):
    ans = []
    for ch in txt:
        if ch == '(':
            ans.append(')')
        else:
            ans.append('(')
    return ''.join(ans)


def recur(p):
    if p == "":
        return ""

    u, v = split_paren(p)
    if is_right(u):
        return u + recur(v)

    ret = '(' + recur(v) + ')' + reverse_paren(u[1:-1])
    return ret


def solution(p):
    answer = recur(p)
    return answer


if __name__ == "__main__":
    print(solution("()(()))("))
