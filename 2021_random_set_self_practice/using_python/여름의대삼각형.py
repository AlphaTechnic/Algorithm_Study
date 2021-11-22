"""
input :
0 0
3 0
0 4

output :
6.00
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    x1, y1 = map(int, input().rstrip().split())
    x2, y2 = map(int, input().rstrip().split())
    x3, y3 = map(int, input().rstrip().split())

    print(f"{abs((x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1)) / 2:.2f}")
