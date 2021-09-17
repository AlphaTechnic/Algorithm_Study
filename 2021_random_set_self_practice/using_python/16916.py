"""
input :
baekjoon
aek

output :
1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def kmp(pat, text):
    table = make_table(pat)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pat[j]:
            j = table[j - 1]

        if text[i] == pat[j]:
            if j == len(pat) - 1:
                return True
            else:
                j += 1
    return False


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


if __name__ == "__main__":
    text = input().rstrip()
    pat = input().rstrip()

    if kmp(pat, text):
        print(1)
    else:
        print(0)
