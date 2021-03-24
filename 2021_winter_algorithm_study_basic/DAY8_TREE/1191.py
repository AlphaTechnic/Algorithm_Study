import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def preorder(root, graph):
    if root in graph:
        l, r = graph[root]
        print(root, end='')
        preorder(l, graph)
        preorder(r, graph)
    else:
        return


def inorder(root, graph):
    if root in graph:
        l, r = graph[root]
        inorder(l, graph)
        print(root, end='')
        inorder(r, graph)
    else:
        return


def postorder(root, graph):
    if root in graph:
        l, r = graph[root]
        postorder(l, graph)
        postorder(r, graph)
        print(root, end='')
    else:
        return


graph = {}
for _ in range(int(input())):
    d, l, r = input().split()
    graph[d] = [l, r]


preorder('A', graph)
print()
inorder('A', graph)
print()
postorder('A', graph)