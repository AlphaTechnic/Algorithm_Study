"""
input :
3
7fwJs`m&+2t*01h
A^T:;9<Z6!*mn@b
'ZNw8<~ALsHYa2]#m0:&IWa

output :
???
A
AaIa
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

chk = {'a', 'e', 'i', 'o', 'u',
       'A', 'E', 'I', 'O', 'U'}

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        txt = input().rstrip()
        flag = False
        for ch in txt:
            if ch in chk:
                flag = True
                print(ch, end='')
        if not flag:
            print("???", end='')
        print()
