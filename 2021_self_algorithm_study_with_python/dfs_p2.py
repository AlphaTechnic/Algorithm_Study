"""
input :
()))((()
ouput :
(()())()
"""

import sys

input = sys.stdin.readline


def is_right_str(string):
    st = []
    for char in string:
        if char == '(':
            st.append('(')
        elif char == ')':
            if len(st) == 0: return False
            if st[-1] != '(': return False
            st.pop()
    return True


def solution(string):  # string = '()))((()'
    if is_right_str(string): return string
    if string == '': return ''

    cnt_left = 0
    cnt_right = 0
    if string[0] == '(': cnt_left += 1
    elif string[0] == ')': cnt_right += 1

    for ind, char in enumerate(string):
        if ind == 0:
            continue

        if char == '(': cnt_left += 1
        elif char == ')': cnt_right += 1

        if cnt_left == cnt_right:
            u = string[:(ind + 1)]
            v = string[(ind + 1):]
            break

    if is_right_str(u):
        return u + solution(v)
    else:
        tmp1 = '(' + solution(v) + ')'
        tmp2 = ''
        for char in u[1:len(u) - 1]:
            if char == '(': tmp2 += ')'
            elif char == ')': tmp2 += '('

        return tmp1 + tmp2
