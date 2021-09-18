"""
input :
2
3 4 3 5
1 1 30
2 3 30
1 2 40
1 2 20
3 1 70
4 4 1 10
1 1 50
2 1 20
1 1 80
3 1 0
1 2 20
2 2 10
4 3 0
2 1 0
2 2 100
1 4 20

output :
1
2
"""
import sys
from collections import defaultdict
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


class TeamScore:
    def __init__(self, pk):
        self.pk = pk
        self.score = defaultdict(int)
        self.tot = 0
        self.last = 0
        self.apply_num = 0

    def feed_score(self, p, score, ind):
        tmp = self.score[p]
        self.score[p] = max(self.score[p], score)
        self.tot += max(0, self.score[p] - tmp)
        self.last = ind
        self.apply_num += 1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, P, ME, Q = map(int, input().rstrip().split())

        teams = []
        # 인덱스 관리를 위해 항상 1등인 dummy object를 하나 만듦
        dummy_obj = TeamScore(0)
        dummy_obj.tot = 10 ** 9
        teams.append(dummy_obj)
        for i in range(1, N + 1):
            obj = TeamScore(i)
            teams.append(obj)

        res = []
        for i in range(1, Q + 1):
            pk, p, score = map(int, input().rstrip().split())
            teams[pk].feed_score(p, score, i)

        teams.sort(key=lambda obj: (- obj.tot, obj.apply_num, obj.last))
        for i, team in enumerate(teams):
            if team.pk == ME:
                print(i)
