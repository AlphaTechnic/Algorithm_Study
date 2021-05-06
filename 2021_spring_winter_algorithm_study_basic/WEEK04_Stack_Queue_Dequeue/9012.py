"""
input :
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

output :
NO
NO
YES
NO
YES
NO
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def is_valid_paren():
    st = []
    for char in line:
        if char == '(':
            st.append('(')
        elif char == ')':
            if len(st) == 0:
                return False
            else:
                st.pop()
    if len(st) != 0:
        return False
    return True


N = int(input())
for _ in range(N):
    line = list(input().rstrip())
    if is_valid_paren():
        print("YES")
    else:
        print("NO")
