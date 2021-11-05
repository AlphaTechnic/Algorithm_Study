"""
input :
3 4
JLA
CRUO
3

output :
CARLUJO
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


class Ant:
    def __init__(self, ch, dir):
        self.ch = ch
        self.dir = dir


if __name__ == "__main__":
    ants = []
    N1, N2 = map(int, input().rstrip().split())
    txt1 = input().rstrip()[::-1]
    for ch in txt1:
        ants.append(Ant(ch, 'r'))
    txt2 = input().rstrip()
    for ch in txt2:
        ants.append(Ant(ch, 'l'))

    # print("origin")
    # for i in range(len(ants)):
    #     print(ants[i].ch, ants[i].dir)
    # print()

    T = int(input())
    for i in range(T):
        j = 0
        while j < len(ants) - 1:
            if ants[j].dir == 'r' and ants[j + 1].dir == 'l':
                ants[j], ants[j + 1] = ants[j + 1], ants[j]
                j += 2
                continue
            j += 1

    for i in range(len(ants)):
        print(ants[i].ch, end='')
    print()
