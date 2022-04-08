from typing import List


class Row(object):
    def __init__(self, me: int):
        self.me = me
        self.up = me - 1
        self.down = me + 1
        self.is_deleted = False

    def __repr__(self):
        if self.is_deleted:
            is_deleted = "X"
        else:
            is_deleted = "O"
        return f"u:({self.up})/{self.me}/d:({self.down})/{is_deleted}"


class Table(object):
    def __init__(self, rows: List[Row], cmds: List[str], k: int):
        self.rows = rows
        self.cmds = cmds
        self.cursor = k
        self.bin = []

    def do_cmds(self):
        for cmd in self.cmds:
            if cmd[0] == 'D':
                self.down(int(cmd[1]))
            elif cmd[0] == 'U':
                self.up(int(cmd[1]))
            elif cmd[0] == 'C':
                self.delete()
            else:
                self.restore()
        return ''.join(["O" if not row.is_deleted else "X" for row in self.rows])

    def delete(self):
        self.bin.append(self.rows[self.cursor])
        self.rows[self.cursor].is_deleted = True
        self.tune_neighbor(self.rows[self.cursor])

        if self.rows[self.cursor].down is not None:
            self.cursor = self.rows[self.cursor].down
        else:
            self.cursor = self.rows[self.cursor].up

    def tune_neighbor(self, row):
        up_row = row.up
        down_row = row.down
        if up_row is not None:
            self.rows[up_row].down = row.down
        if down_row is not None:
            self.rows[down_row].up = row.up

    def up(self, cnt):
        while cnt != 0:
            self.cursor = self.rows[self.cursor].up
            cnt -= 1

    def down(self, cnt):
        while cnt != 0:
            self.cursor = self.rows[self.cursor].down
            cnt -= 1

    def restore(self):
        row = self.bin.pop()
        self.rows[row.me].is_deleted = False
        up_row = self.rows[row.me].up
        down_row = self.rows[row.me].down

        if up_row is not None:
            self.rows[up_row].down = row.me
        if down_row is not None:
            self.rows[down_row].up = row.me


def solution(n, k, cmd):
    # row 준비
    rows = [Row(i) for i in range(n)]
    rows[0].up = None
    rows[-1].down = None

    cmds = [command.split() for command in cmd]
    table = Table(rows, cmds, k)
    return table.do_cmds()


if __name__ == "__main__":
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
    print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
