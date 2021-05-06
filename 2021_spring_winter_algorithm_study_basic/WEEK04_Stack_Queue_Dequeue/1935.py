"""
input :
5
ABC*+DE/-
1
2
3
4
5

ouput :
6.20
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
expr = input().rstrip()

operands = dict()
for i in range(65, 91):
    operands[chr(i)] = 0
for i in range(N):
    operands[chr(65 + i)] = int(input())

st = []
for char in expr:
    if 65 <= ord(char) <= 90:
        st.append(operands[char])
    else:
        oper = char
        operand2 = st.pop()
        operand1 = st.pop()

        if oper == "*":
            st.append(operand1 * operand2)
        elif oper == "+":
            st.append(operand1 + operand2)
        elif oper == "-":
            st.append(operand1 - operand2)
        elif oper == "/":
            st.append(operand1 / operand2)

print("%.2f" % st[0])