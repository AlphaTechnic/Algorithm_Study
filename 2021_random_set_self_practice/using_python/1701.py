"""
input :
abcdabcabb

output :
3
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_table(pat):
    table = [0 for _ in range(len(pat))]
    j = 0
    for i in range(1, len(pat)):
        while j > 0 and pat[j] != pat[i]:
            j = table[j - 1]

        if pat[i] == pat[j]:
            j += 1
            table[i] = j
    return table


if __name__ == "__main__":
    text = input().rstrip()
    max_val = -1
    for i in range(len(text)):
        # print(make_table(text[i:]))
        max_val = max(max_val, max(make_table(text[i:])))

    print(max_val)
