"""
input :
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0

output :
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
"""

import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

while True:
    line = list(map(int, input().rstrip().split()))
    k = line[0]
    S = line[1:]
    if line[0] == 0: break

    for a1, a2, a3, a4, a5, a6 in list(combinations(S, 6)):
        print(a1, a2, a3, a4, a5, a6)
    print()
