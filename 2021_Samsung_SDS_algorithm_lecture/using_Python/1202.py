"""
input :
3 2
1 65
5 23
2 99
10
2

output :
164
"""

import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def get_max_val():
    max_heap = []
    tot = 0
    idx = 0
    for bag_capicity in bags:
        # bag_capicity 이하의 weight를 가진 보석들을 max heap에 쓸어 담는다.
        for i in range(idx, len(jewels)):
            if jewels[i][0] <= bag_capicity:
                heapq.heappush(max_heap, -jewels[i][1])
                idx += 1
            else:
                break

        if len(max_heap) != 0:
            tot += -heapq.heappop(max_heap)

    return tot


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())

    jewels = []
    bags = []
    for _ in range(N):
        jewels.append(list(map(int, input().rstrip().split())))
    for _ in range(K):
        bags.append(int(input()))

    jewels.sort()
    bags.sort()

    print(get_max_val())