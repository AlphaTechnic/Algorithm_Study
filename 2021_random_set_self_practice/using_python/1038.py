"""
input :
18

output :
42
"""
import sys
from itertools import combinations

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

seed = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    res = []
    for i in range(1, 11):
        for combi in combinations(seed, i):
            res.append(int(''.join(map(str, sorted(list(combi), reverse=True)))))
    res.sort()

    N = int(input())
    if N <= 1022:
        print(res[N])
    else:
        print(-1)
