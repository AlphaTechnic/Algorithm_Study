"""
input :
33(562(71(9)))

output :
19
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(s, e):
    length = 0

    idx = s
    while idx < e:
        if text[idx] == '(':
            length += int(text[idx - 1]) * recur(idx + 1, paren[idx]) - 1
            idx = paren[idx]
        else:
            length += 1

        idx += 1

    return length


if __name__ == "__main__":
    text = input().rstrip()
    st = list()
    paren = [0 for _ in range(50)]
    for i in range(len(text)):
        if text[i] == '(':
            st.append(i)
        elif text[i] == ')':
            paren[st.pop()] = i

    print(recur(0, len(text)))
