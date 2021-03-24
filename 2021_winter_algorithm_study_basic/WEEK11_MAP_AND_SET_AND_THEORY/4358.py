import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

trees = []
total = 0
while True:
    try:
        trees.append(input())
        total += 1
    except EOFError:
        break

trees_cnt = Counter(trees)
for tree in sorted(list(Counter(trees).keys())):
    # print(tree, round((trees_cnt[tree] / total) * 100, 4))
    print("%s %.4f" % (tree, (trees_cnt[tree] / total) * 100))
