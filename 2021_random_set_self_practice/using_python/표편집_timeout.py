from typing import List


class Row(object):
    def __init__(self, num, exsist=True):
        self.num = num
        self.exsist = exsist

    def __repr__(self):
        is_in = "O" if self.exsist else "X"
        return f"{self.num}/{is_in}"


class Table(object):
    def __init__(self, rows: List[Row], start: int, cmds: List[str]):
        self.rows = rows
        self.N = len(rows)
        self.cur = start
        self.cmds = cmds
        self.recycle_bin = []

    def do_cmds(self):
        for cmd in self.cmds:
            if cmd[0] == 'D':
                k = int(cmd[1])
                self.down(k)
            elif cmd[0] == 'C':
                self.delete()
            elif cmd[0] == 'U':
                k = int(cmd[1])
                self.up(k)
            elif cmd[0] == 'Z':
                self.restore()

        def to_OX(exist: bool):
            if exist:
                return "O"
            return "X"

        return ''.join(map(to_OX, [row.exsist for row in self.rows]))

    def down(self, k):
        if self.is_last(self.cur):
            self.cur = self.find_last_idx()
            return

        cnt = 0
        while True:
            self.cur += 1
            if not self.rows[self.cur].exsist:
                continue

            cnt += 1
            if cnt == k or self.is_last(self.cur):
                break

    def up(self, k):
        cnt = 0
        while True:
            self.cur -= 1
            if not self.rows[self.cur].exsist:
                continue

            cnt += 1
            if cnt == k:
                break

    def delete(self):
        self.rows[self.cur].exsist = False
        self.recycle_bin.append(self.rows[self.cur].num)
        self.down(1)

    def restore(self):
        idx_to_recycle = self.recycle_bin.pop()
        self.rows[idx_to_recycle].exsist = True

    def is_last(self, cur):
        for i in range(cur, self.N):
            if self.rows[i].exsist:
                return False
        return True

    def find_last_idx(self):
        for i in range(self.N - 1, -1, -1):
            if self.rows[i].exsist:
                return self.rows[i].num


def solution(n, k, cmd):
    rows = [Row(i) for i in range(n)]
    cmds = [c.split() for c in cmd]
    table = Table(rows, k, cmds)
    return table.do_cmds()


if __name__ == "__main__":
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
