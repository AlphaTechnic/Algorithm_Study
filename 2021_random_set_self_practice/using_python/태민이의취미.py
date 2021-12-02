"""
input :
10

output :
3025
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

MOD = 1000000007

if __name__ == "__main__":
    N = int(input())
    print(((N ** 2 * (N + 1) ** 2) // 4) % MOD)
