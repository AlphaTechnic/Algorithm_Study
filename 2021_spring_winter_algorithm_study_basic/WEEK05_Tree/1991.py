"""
input :
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .

output :
ABDCEFG
DBAECFG
DBEGFCA
"""

import sys

sys.setrecursionlimit(10 ** 8)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N = int(input().rstrip())
graph = dict()
for _ in range(N):
    p, c1, c2 = input().rstrip().split()
    graph[p] = [c1, c2]


def preorder(S):
    if S == '.':
        return
    print(S, end='')
    preorder(graph[S][0])
    preorder(graph[S][1])


def inorder(S):
    if S == '.':
        return
    inorder(graph[S][0])
    print(S, end='')
    inorder(graph[S][1])


def postorder(S):
    if S == '.':
        return
    postorder(graph[S][0])
    postorder(graph[S][1])
    print(S, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
