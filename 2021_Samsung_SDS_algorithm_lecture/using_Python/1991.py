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
sys.setrecursionlimit(10**8)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())

graph = dict()
for _ in range(N):
    v, l, r = input().rstrip().split()
    graph[v] = [l, r]


def preorder(root):
    if root == '.':
        return

    print(root, end='')
    preorder(graph[root][0])
    preorder(graph[root][1])


def inorder(root):
    if root == '.':
        return

    inorder(graph[root][0])
    print(root, end='')
    inorder(graph[root][1])


def postorder(root):
    if root == '.':
        return

    postorder(graph[root][0])
    postorder(graph[root][1])
    print(root, end='')


if __name__ == "__main__":
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
    print()

