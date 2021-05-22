"""
input :
5
ABC*+DE/-
1
2
3
4
5

output :
6.20
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

variables = dict()
for i in range(65, 91):
    variables[chr(i)] = 0

N = int(input())
expr = input().rstrip()

ind = 65
for _ in range(N):
    variables[chr(ind)] = int(input())
    ind += 1

st = []
for op in expr:
    if 65 <= ord(op) <= 90:  # var
        st.append(variables[op])
    else:
        op2 = st.pop()
        op1 = st.pop()
        if op == '*':
            st.append(op1 * op2)
        elif op == '+':
            st.append(op1 + op2)
        elif op == '-':
            st.append(op1 - op2)
        elif op == '/':
            st.append(op1 / op2)

print("%0.2f" % st[0])
