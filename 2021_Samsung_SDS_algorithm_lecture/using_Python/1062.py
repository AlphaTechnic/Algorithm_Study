"""
input :
3 6
antarctica
antahellotica
antacartica

output :
2
"""

import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())

# words : 각 단어를 '비트마스킹으로 상징'하여 저장
words = [0 for _ in range(N)]
for combi in range(N):
    tmp = input().rstrip()

    # word 배열에 각 문자의 비트마스킹 저장
    for ch in tmp:
        words[combi] = words[combi] | (1 << (ord(ch) - ord('a')))

# edge cases
if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()


# candidiate : 필수 글자를 제외한 알파벳
# need : 필수 알파벳
candidiate = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
need = ['a', 'c', 't', 'i', 'n']
max_val = 0
for combi in list(combinations(candidiate, K - 5)):
    each = 0
    tmp_val = 0

    # 각 combi을 비트마스킹으로 상징
    for ch in need:
        each = each | (1 << (ord(ch) - ord('a')))
    for ch in combi:
        each = each | (1 << (ord(ch) - ord('a')))

    # 단어와 각 조합의 비교
    for word in words:
        if each & word == word:  # each <(포함) word
            tmp_val += 1

    max_val = max(max_val, tmp_val)

print(max_val)