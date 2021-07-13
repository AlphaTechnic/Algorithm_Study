"""
input :
80875542

output :
88755420
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

digits = list(map(int, input().rstrip()))

if 0 not in digits:
    print(-1)
    exit()

if sum(digits) % 3 != 0:
    print(-1)
    exit()

digits.sort(reverse=True)
for digit in digits:
    print(digit, end='')
