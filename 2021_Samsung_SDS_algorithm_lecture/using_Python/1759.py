"""
input :
4 6
a t c i s w

output :
acis
acit
aciw
acst
acsw
actw
aist
aisw
aitw
astw
cist
cisw
citw
istw
"""

import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

line_len, type_num = map(int, input().rstrip().split())
indices = [i for i in range(type_num)]
alphabets = input().rstrip().split()
alphabets.sort()
aeiou_set = {'a', 'e', 'i', 'o', 'u'}

for inds in list(combinations(indices, line_len)):
    # 조건 만족 못하면 쪼까냄
    aeiou_num = 0
    comple_of_aeiou_num = 0
    for ind in inds:
        if alphabets[ind] in aeiou_set:
            aeiou_num += 1
        else:
            comple_of_aeiou_num += 1
    if aeiou_num < 1: continue
    if comple_of_aeiou_num < 2: continue

    # 출력
    for ind in inds:
        print(alphabets[ind], end='')
    print()
