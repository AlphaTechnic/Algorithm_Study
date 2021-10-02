"""
input :
Union of Computer Programming Contest club contest

output :
I love UCPC
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find_char(txt, ch):
    for i in range(len(txt)):
        if txt[i] == ch:
            return i
    return -1


def chk(txt):
    i = find_char(txt, 'U')
    txt = txt[i:]
    if i == -1:
        return False

    i = find_char(txt, 'C')
    txt = txt[i:]
    if i == -1:
        return False

    i = find_char(txt, 'P')
    txt = txt[i:]
    if i == -1:
        return False

    i = find_char(txt, 'C')
    txt = txt[i:]
    if i == -1:
        return False

    return True


if __name__ == "__main__":
    txt = input().rstrip()
    if chk(txt):
        print("I love UCPC")
    else:
        print("I hate UCPC")