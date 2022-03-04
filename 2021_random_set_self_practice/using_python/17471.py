import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def mk_choices(num):
    choices = set()
    choice = 1
    while num != 0:
        if num & 1:
            choices.add(choice)
        num >>= 1
        choice += 1
    return choices


def connection_chk_by_bfs(graph, choices):
    start = list(choices)[0]
    tot = nums[start]
    cnt = 1

    visited = [False for _ in range(N + 1)]
    que = deque()
    visited[start] = True
    que.append(start)

    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if nxt in choices and not visited[nxt]:
                cnt += 1
                tot += nums[nxt]

                que.append(nxt)
                visited[nxt] = True

    if cnt == len(choices):  # means all connected
        return tot
    else:
        return -1


def divide(graph, choices):
    # test 1 : 선택된 애들 모두 연결되어 있는지
    tot1 = connection_chk_by_bfs(graph, choices)
    if tot1 == -1:
        return -1

    # test 2: 안 선택된 애들 모두 연결되어 있는지
    comple = set([i for i in range(1, N + 1)]) - choices
    tot2 = connection_chk_by_bfs(graph, comple)
    if tot2 == -1:
        return -1

    return abs(tot1 - tot2)


if __name__ == "__main__":
    N = int(input())
    nums = ['_'] + list(map(int, input().rstrip().split()))

    graph = defaultdict(list)
    for i in range(1, N + 1):
        info = list(map(int, input().rstrip().split()))
        graph[i].extend(info[1:])

    min_diff = 10 ** 7
    for i in range(1, 1 << N - 1):
        choices = mk_choices(i)
        res = divide(graph, choices)
        if res != -1:
            min_diff = min(min_diff, res)

    if min_diff == 10 ** 7:
        print(-1)
    else:
        print(min_diff)
