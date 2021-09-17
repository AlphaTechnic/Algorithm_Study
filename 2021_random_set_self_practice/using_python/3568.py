"""
input :
int& a*[]&, b, c*;

output :
int&&[]* a;
int& b;
int&* c;
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_reverse(text):
    dq = deque()
    ind = 0
    while ind < len(text) - 1:
        if text[ind] == '[':
            dq.appendleft("[]")
            ind += 2
            continue
        dq.appendleft(text[ind])
        ind += 1
    return ''.join(dq)


def parse(text):
    ind = 0
    reversed_symbol = ""
    for i in range(len(text)):
        if text[i] in builtin_symbols:
            ind = i
            reversed_symbol += make_reverse(text[i:])
            break
    return text[:ind], reversed_symbol


if __name__ == "__main__":
    builtin_symbols = {'*', '[', '&', ',', ';'}
    text = input().rstrip().split(' ')
    base = text[0]

    for i in range(1, len(text)):
        name, reversed_symbol = parse(text[i])
        new_base = base + reversed_symbol
        print(new_base + ' ' + name + ';')
