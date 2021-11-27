"""
input :
5
0.000 0.000
1.000 1.000
2.000 0.000
3.000 1.500
2.235 2.483

output :
RIGHT
LEFT
LEFT
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


class Prisoner(object):
    def __init__(self):
        self.N = -1
        self.seq = []

    def input(self):
        self.N = int(input())
        for _ in range(self.N):
            x, y = map(float, input().rstrip().split())
            self.seq.append((x, y))

    def ccw(self, p1, p2, p3):
        ret = (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p2[1] - p1[1]) * (p3[0] - p2[0])
        if ret > 0:
            return 1
        elif ret < 0:
            return -1
        else:
            return 0

    def go(self):
        idx = 0
        while idx != len(self.seq) - 2:
            ret = self.ccw(self.seq[idx], self.seq[idx + 1], self.seq[idx + 2])
            if ret == 1:
                print("LEFT")
            elif ret == -1:
                print("RIGHT")
            else:
                print("error")
            idx += 1


if __name__ == "__main__":
    prisoner = Prisoner()
    prisoner.input()
    prisoner.go()
