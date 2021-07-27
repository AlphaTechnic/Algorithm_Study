"""
input :
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

output :
0
"""

import sys
from itertools import combinations
from itertools import permutations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    seed = [i for i in range(N)]
    board = list()
    for _ in range(N):
        board.append(list(map(int, (input().rstrip().split()))))

    combi = list(combinations(seed, N // 2))
    min_val = 1000
    for i in range(len(combi) // 2):
        tot1 = 0
        tot2 = 0
        for a, b in permutations(combi[i], 2):
            tot1 += board[a][b]
        for a, b in permutations(combi[len(combi) - i - 1], 2):
            tot2 += board[a][b]
        min_val = min(min_val, abs(tot1 - tot2))
    print(min_val)
