import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
parent = list(map(int, sys.stdin.readline().split()))
del_node = int(sys.stdin.readline())
tree = {}

for i in range(N):
    if i == del_node or parent[i] == del_node:
        continue

    if parent[i] in tree:
        tree[parent[i]].append(i)
    else:
        tree[parent[i]] = [i]

num_of_leaves = 0
stack = []
if -1 in tree:
    stack.append(-1)

while len(stack) != 0:
    node = stack.pop()

    if node not in tree:
        num_of_leaves += 1
    else:
        stack += tree[node]

print(num_of_leaves)