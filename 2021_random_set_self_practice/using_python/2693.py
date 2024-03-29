"""
input :
4
1 2 3 4 5 6 7 8 9 1000
338 304 619 95 343 496 489 116 98 127
931 240 986 894 826 640 965 833 136 138
940 955 364 188 133 254 501 122 768 408

output :
8
489
931
768
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        tmp = list(map(int, input().rstrip().split()))
        tmp.sort(reverse=True)
        print(tmp[2])
