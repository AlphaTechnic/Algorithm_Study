"""
input :
4 2

output :
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4
"""
import sys
from itertools import product

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())

    for combi in product([i for i in range(1, N + 1)], repeat=M):
        for num in combi:
            print(num, end=' ')
        print()
