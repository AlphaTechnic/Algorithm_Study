"""
input :
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
word_list = []
for _ in range(N):
    word_list.append(input().rstrip())

word_list = list(set(word_list))
word_list.sort(key=lambda x: (len(x), x))
for word in word_list:
    print(word)