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
ALPHABETS = input().rstrip().split()
ALPHABETS.sort()
aeiou_set = {'a', 'e', 'i', 'o', 'u'}


def is_valid():
    aeiou_num = 0
    comple_of_aeiou_num = 0
    for ind in inds:
        if ALPHABETS[ind] in aeiou_set:
            aeiou_num += 1
        else:
            comple_of_aeiou_num += 1
    if aeiou_num < 1: return False
    if comple_of_aeiou_num < 2: return False

    return True


for inds in list(combinations(indices, line_len)):
    if is_valid():
        # 출력
        for ind in inds:
            print(ALPHABETS[ind], end='')
        print()
