"""
input :
B
ABBA

output :
1
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def TAR_to_S(text):
    global S
    while len(text) != len(S):
        if text[-1] == 'A':
            text = text[:-1]
        elif text[-1] == 'B':
            text = text[:-1][::-1]

    if text == S:
        return True
    else:
        return False


if __name__ == "__main__":
    S = input().rstrip()
    TAR = input().rstrip()

    if TAR_to_S(TAR):
        print(1)
    else:
        print(0)
