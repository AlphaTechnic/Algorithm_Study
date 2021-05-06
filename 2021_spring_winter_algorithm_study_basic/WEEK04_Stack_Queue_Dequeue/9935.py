"""
input :
umssusummhum
sum

output :
umshum
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

String = input().rstrip()
pat = input().rstrip()
# rough한 구현 -> O(n^2) 시간초과
# while pat in String:
#     String = String.replace(pat, "")

st = []
for char in String:
    st.append(char)
    if char == pat[-1]:
        for i in range(len(pat)):
            if len(st) == 0:
                st.extend(pat[-i:])  # 폭발 중단 -> 원상 복구
                break
            else:
                if pat[-1-i] != st[-1]:
                    st.extend(pat[-i:])  # 폭발 중단 -> 원상 복구
                    break
                else:
                    st.pop()

if len(st) == 0:
    print("FRULA")
else:
    print("".join(st))
