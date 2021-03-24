import sys
sys.stdin = open("input.txt", "r")

N = int(input())
expression = list(input())
num_list = [int(input()) for _ in range(N)]
st = []

# 대문자 아스키코드 65~90
pre_operand = '!'
for ch in expression:
    if 65 <= ord(ch) <= 90:
        st.append(num_list[ord(ch) - ord('A')])
    else:
        operand2 = st.pop()
        operand1 = st.pop()
        if ch == '+':
            res = operand1 + operand2
            st.append(res)
        elif ch == '-':
            res = operand1 - operand2
            st.append(res)
        elif ch == '*':
            res = operand1 * operand2
            st.append(res)
        elif ch == '/':
            res = operand1 / operand2
            st.append(res)
print("%0.2f" % st[0])