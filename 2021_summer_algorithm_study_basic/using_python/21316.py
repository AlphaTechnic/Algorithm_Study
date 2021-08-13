"""
input :
1 2
2 3
3 4
4 5
3 7
4 9
6 7
7 8
9 8
9 10
10 11
12 11

output :
7
"""
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

if __name__ == "__main__":
    graph = dict()
    for i in range(1, 13):
        graph[i] = list()

    for _ in range(12):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    outdeg3 = []
    for i in graph:
        if len(graph[i]) == 3:
            outdeg3.append(i)

    ans = -1
    for nd in outdeg3:
        cnt = 0
        for nxt in graph[nd]:
            cnt += len(graph[nxt])
        if cnt == 6:
            ans = nd
            break
    print(ans)
