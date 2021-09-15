"""
input :
1
13
OOIOIOIOIIOII

output :
4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_pat(i):
    pat = list('I')
    while i != 0:
        pat.append('O')
        pat.append('I')
        i -= 1

    return pat


def make_table(pat):
    table = [0 for _ in range(len(pat))]

    j = 0
    for i in range(1, len(pat)):
        while j > 0 and pat[i] != pat[j]:
            j = table[j - 1]
        if pat[i] == pat[j]:
            j += 1
            table[i] = j
    return table


def kmp(text, pat):
    table = make_table(pat)

    cnt = 0
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pat[j]:
            j = table[j - 1]

        if text[i] == pat[j]:
            if j == len(pat) - 1:
                j = table[j]
                cnt += 1
            else:
                j += 1
    return cnt


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    text = list(input().rstrip())

    pat = make_pat(N)
    print(kmp(text, pat))
