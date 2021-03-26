"""
input :
4 6
a t c i s w
"""


import sys
import itertools
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

r, n = map(int, input().split())
alphabets = list(input().split())
alphabets.sort()

ans = list(itertools.combinations(alphabets, r))
ans.sort()

for res in ans:
    num_of_aeiou = 0
    for char in res:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            num_of_aeiou += 1
    num_of_others = r - num_of_aeiou
    if num_of_aeiou < 1: continue
    if num_of_others < 2: continue

    for digit in res:
        print(digit, end='')
    print()
