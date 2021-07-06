"""
input :
DUP
MUL
NUM 2
ADD
END
3
1
10
50

NUM 1
NUM 1
ADD
END
2
42
43

NUM 600000000
ADD
END
3
0
600000000
1

QUIT

output :
3
102
2502

ERROR
ERROR

600000000
ERROR
600000001
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

MAX = 10**9 + 1


def NUM(arg):
    GOSTACK.append(arg)


def POP():
    try:
        return GOSTACK.pop()
    except:
        return MAX


def INV():
    try:
        GOSTACK[-1] *= -1
    except:
        return MAX


def DUP():
    try:
        GOSTACK.append(GOSTACK[-1])
    except:
        return MAX


def SWP():
    try:
        GOSTACK[-1], GOSTACK[-2] = GOSTACK[-2], GOSTACK[-1]
    except:
        return MAX


def ADD():
    try:
        a1 = GOSTACK.pop()
        a2 = GOSTACK.pop()
        res = a1 + a2
        if abs(res) < MAX:
            GOSTACK.append(res)
        else:
            raise Exception()
    except:
        return MAX


def SUB():
    try:
        a1 = GOSTACK.pop()
        a2 = GOSTACK.pop()
        res = a2 - a1
        if abs(res) < MAX:
            GOSTACK.append(res)
        else:
            raise Exception()
    except:
        return MAX


def MUL():
    try:
        a1 = GOSTACK.pop()
        a2 = GOSTACK.pop()
        res = a2 * a1
        if abs(res) < MAX:
            GOSTACK.append(res)
        else:
            raise Exception()
    except:
        return MAX


def DIV():
    try:
        a1 = GOSTACK.pop()
        a2 = GOSTACK.pop()

        if a1*a2 < 0 : s = -1
        elif a1*a2 == 0 : s = 0
        else: s = 1

        res = (abs(a2) // abs(a1)) * s
        if abs(res) < MAX:
            GOSTACK.append(res)
        else:
            raise Exception()
    except:
        return MAX


def MOD():
    try:
        a1 = GOSTACK.pop()
        a2 = GOSTACK.pop()

        if a2 < 0: s = -1
        elif a2 == 0: s = 0
        else: s = 1

        res = (abs(a2) % abs(a1)) * s
        if abs(res) < MAX:
            GOSTACK.append(res)
        else:
            raise Exception()
    except:
        return MAX


FUN_DIC = {
    "NUM": NUM,
    "POP": POP,
    "INV": INV,
    "DUP": DUP,
    "SWP": SWP,
    "ADD": ADD,
    "SUB": SUB,
    "MUL": MUL,
    "DIV": DIV,
    "MOD": MOD,
}


first_flag = 1
while True:
    GOSTACK = []
    PROGRAM = []
    while True:
        cmd = input().rstrip()
        if cmd == "END": break
        elif cmd == "QUIT": exit()

        PROGRAM.append(cmd)

    N = int(input())
    for _ in range(N):
        GOSTACK = []
        GOSTACK.append(int(input()))
        for cmd in PROGRAM:
            if cmd[0] == 'N':
                arg = int(cmd.split()[-1])
                if FUN_DIC['NUM'](arg) == MAX:
                    GOSTACK = []
                    print("ERROR")
                    break
            else:
                if FUN_DIC[cmd]() == MAX:
                    GOSTACK = []
                    print("ERROR")
                    break
        else:
            if len(GOSTACK) == 1:
                print(GOSTACK[0])
            else:
                print("ERROR")

    input()
    print()
