"""
input :
3
FFLF
FFRRFF
FFFBBBRFFFBBB

output :
2
0
9
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

DIR = [(1, 0), (0, -1), (-1, 0), (0, 1)]


class Turtle:
    def __init__(self):
        self.pos = (0, 0)
        self.dir = 3
        self.xrange = [0, 0]
        self.yrange = [0, 0]
        self.area = 0

    def action(self, cmd):
        if cmd == 'F':
            dx, dy = DIR[self.dir]
            cx, cy = self.pos
            self.pos = cx + dx, cy + dy
        elif cmd == 'B':
            backward = (self.dir + 2) % 4
            dx, dy = DIR[backward]
            cx, cy = self.pos
            self.pos = cx + dx, cy + dy
        elif cmd == 'L':
            self.dir = (self.dir + 3) % 4
        elif cmd == 'R':
            self.dir = (self.dir + 1) % 4
        self.update()

    def update(self):
        self.xrange[0] = min(self.xrange[0], self.pos[0])
        self.xrange[1] = max(self.xrange[1], self.pos[0])
        self.yrange[0] = min(self.yrange[0], self.pos[1])
        self.yrange[1] = max(self.yrange[1], self.pos[1])
        self.area = (self.xrange[1] - self.xrange[0]) * (self.yrange[1] - self.yrange[0])


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        cmds = input().rstrip()
        turtle = Turtle()
        for cmd in cmds:
            turtle.action(cmd)
        print(turtle.area)
