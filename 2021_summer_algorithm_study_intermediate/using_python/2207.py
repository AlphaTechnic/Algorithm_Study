"""
input :
2 1
1 1
-1 -1

output :
OTL
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    