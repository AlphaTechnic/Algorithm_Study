"""
input :
level
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

string = input().rstrip()
l = 0
r = len(string) - 1

ans = 1
while l < r:
    if string[l] != string[r]:
        ans = 0
        break
    l += 1
    r -= 1

print(ans)
