"""
input :
02984

output :
576
"""

import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

digits = input()
N = len(digits)

max_val = 0
val = int(digits[0])
def find_maxval(lv, operand):
    global max_val
    global val
    if lv == N - 1:
        max_val = max(max_val, operand)
        return

    val += int(digits[lv + 1])
    find_maxval(lv + 1, val)
    val -= int(digits[lv + 1])

    if digits[lv + 1] != '0':
        val *= int(digits[lv + 1])
        find_maxval(lv + 1, val)
        val = val // int(digits[lv + 1])


find_maxval(0, int(digits[0]))
print(max_val)
