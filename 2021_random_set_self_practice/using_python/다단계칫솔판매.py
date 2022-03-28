import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 8)


class Selling(object):
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return f"{self.name}/{self.amount}"


class Graph(object):
    def __init__(self, graph, sell_seq, enroll):
        self.enroll = enroll
        self.graph = graph

        self.sell_seq = sell_seq
        self.results = defaultdict(int)

    def manage_selling(self):
        for selling in self.sell_seq:
            self.broadcast(selling.name, selling.amount)
        return [self.results[name] for name in self.enroll]

    def broadcast(self, name, money):
        to_give = money // 10
        to_have = money - to_give
        self.results[name] += to_have
        if to_give == 0:
            return
        if name != '-':
            self.broadcast(self.graph[name], to_give)


def solution(enroll, referral, seller, amount):
    graph = defaultdict(str)
    for i in range(len(enroll)):
        graph[enroll[i]] = referral[i]
    sell_seq = []
    for i in range(len(seller)):
        sell_seq.append(Selling(seller[i], amount[i] * 100))
    g = Graph(graph, sell_seq, enroll)
    return g.manage_selling()


if __name__ == "__main__":
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                   ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                   ["sam", "emily", "jaimie", "edward"],
                   [2, 3, 5, 4]))
    print(solution(["john"], ["-"], ["john"], [2]))
