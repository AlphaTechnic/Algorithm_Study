"""
input :
2
5
1 1 0 1
0 0 0
0 1
1
5
1 1 1 1
0 0 1
0 1
1

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
        N = int(input())
        match = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        for i in range(1, N):
            line = list(map(int, input().rstrip().split()))
            ind = 0
            for j in range(i + 1, N + 1):
                match[j][i] = match[i][j] = line[ind]
                ind += 1

        triangle_num = (N * (N - 1) * (N - 2)) // 6
        two_color_triangle_num = 0
        for i in range(1, N + 1):
            color1_num = sum(match[i])
            two_color_triangle_num += color1_num * ((N - 1) - color1_num)

        two_color_triangle_num >>= 1
        print(triangle_num - two_color_triangle_num)
