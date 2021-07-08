"""
input :
2
GCF
ACDEB

output :
99437
"""

"""
포인트 1.
경우의 수 만들기

포인트 2.
문자 - 숫자 mapping

포인트 3.
합 구하기
"""

import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
words = []
unions = set()
for _ in range(N):
    word = list(input().rstrip())
    words.append(word)
    unions |= set(word)

chars = list(unions)
nums = [i + (10 - len(chars)) for i in range(len(chars))]
nums_perm = permutations(nums, len(nums))

# print(words)
# print(chars)
# print(nums)
# print(nums_perm)
#
# 문자 - 숫자 matching
ans = 0
for num_seq in nums_perm:
    char_num_dic = dict()

    for ch, num in zip(chars, num_seq):
        char_num_dic[ch] = num

    # calc
    tot = 0
    for word in words:
        line_val = ""
        for var in word:
            ch_val = str(char_num_dic[var])
            line_val += ch_val
        tot += int(line_val)
    ans = max(tot, ans)

print(ans)
