"""
input :
A+B*C-D/E

output :
ABC*+DE/-
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

expr_infix = input().rstrip()
eval = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 3}

st = []
for op in expr_infix:
    if 65 <= ord(op) <= 90:
        print(op, end='')
    else:
        if op == '(':
            st.append(op)
        elif op == ')':
            while True:
                operator = st.pop()
                if operator == '(':
                    break
                print(operator, end='')
        else:
            while True:
                if len(st) == 0:
                    st.append(op)
                    break

                op_in_st = st[-1]
                if eval[op] <= eval[op_in_st]:
                    print(st.pop(), end='')
                else:
                    st.append(op)
                    break

while len(st) != 0:
    print(st.pop(), end='')
