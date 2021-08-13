"""
input :
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5

output :
2
4
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().rstrip().split())
        for _ in range(E):
            input()
        print(V - 1)
