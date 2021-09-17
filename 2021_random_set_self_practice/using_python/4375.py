"""
input :
3
7
9901

output:
3
6
12
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    try:
        while True:
            N = int(input())
            ones = ['1']
            while True:
                if int(''.join(ones)) % N == 0:
                    print(len(ones))
                    break
                ones.append('1')
    except:
        exit(0)
