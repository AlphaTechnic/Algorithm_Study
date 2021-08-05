"""
input :
4
2 3 1
5 2 4 1

output :
18
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dists = list(map(int, input().rstrip().split()))
    costs = list(map(int, input().rstrip().split()))

    min_cost = costs[0]
    tot_dist = 0
    tot_cost = 0
    for i in range(1, len(costs)):
        tot_dist += dists[i - 1]
        if costs[i] < min_cost:
            tot_cost += tot_dist * min_cost
            min_cost = costs[i]
            tot_dist = 0
        elif i == len(costs) - 1:
            tot_cost += tot_dist * min_cost

    print(tot_cost)
