"""
input :
0001100

output :
1
"""

import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

S = input()
def find_num_of_changes(a, b):
    cnt = 0
    if S[0] == b:
        cnt += 1
    for i in range(len(S) - 1):
        if S[i] == a and S[i + 1] == b:
            cnt += 1
    return cnt

print(min(find_num_of_changes('0', '1'), find_num_of_changes('1', '0')))
