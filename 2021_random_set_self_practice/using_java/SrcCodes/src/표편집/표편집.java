package 표편집;

class Row {
    int up;
    int me;
    int down;
    boolean is_deleted = false;
}

class Table {
    Row[] rows;
    int cur;
    String[] cmds;
    Row[] bin;
    int bin_idx = 0;

    public Table(Row[] rows, int start, String[] cmds) {
        this.rows = rows;
        this.cur = start;
        this.cmds = cmds;
        this.bin = new Row[this.rows.length];
    }

    public String doAllCmds() {
        for (String cmd: this.cmds) {
            char action = cmd.charAt(0);
            int k;
            switch (action) {
                case 'U':
                    k = Integer.parseInt(cmd.substring(2));
                    this.up(k);
                    break;
                case 'D':
                    k = Integer.parseInt(cmd.substring(2));
                    this.down(k);
                    break;
                case 'C':
                    this.delete();
                    break;
                case 'Z':
                    this.restore();
                    break;
                default:
                    // something wrong
                    assert (false) : "unknown type";
            }
        }

        // return ans
        StringBuilder ans = new StringBuilder();
        for (Row row: this.rows) {
            if (row.is_deleted) {
                ans.append('X');
            }
            else {
                ans.append('O');
            }
        }
        return ans.toString();
    }

    public void down(int k) {
        while (k != 0) {
            this.cur = this.rows[this.cur].down;
            k--;
        }
    }

    public void up (int k) {
        while (k != 0) {
            this.cur = this.rows[this.cur].up;
            k--;
        }
    }

    public void delete() {
        // delete 마킹 and 휴지통으로
        this.rows[this.cur].is_deleted = true;
        this.bin[this.bin_idx++] = rows[this.cur];

        // delete 내용 위row, 아래row에 전파
        int up_idx = this.rows[this.cur].up;
        int down_idx = this.rows[this.cur].down;
        if (up_idx != -1) {
            this.rows[up_idx].down = this.rows[this.cur].down;
        }
        if (down_idx != -1) {
            this.rows[down_idx].up = this.rows[this.cur].up;
        }

        // cursor 조정
        if (this.rows[this.cur].down == -1) {  // last row
            this.cur = this.rows[this.cur].up;
        }
        else {
            this.cur = this.rows[this.cur].down;
        }
    }

    public void restore() {
        // delete 마킹 해제 and 휴지통에서 꺼내옴
        Row tarRow = this.bin[--this.bin_idx];
        this.rows[tarRow.me].is_deleted = false;

        // 복구 내용 위row, 아래row에 전파
        int up_idx = tarRow.up;
        int down_idx = tarRow.down;
        if (up_idx != -1) {
            this.rows[up_idx].down = tarRow.me;
        }
        if (down_idx != -1) {
            this.rows[down_idx].up = tarRow.me;
        }
    }
}

class Solution {
    public String solution(int n, int k, String[] cmd) {
        Row[] rows = new Row[n];
        for (int idx = 0; idx < n; idx++) {
            Row row = new Row();
            row.me = idx;
            row.up = idx - 1;
            row.down = idx + 1;
            rows[idx] = row;
        }
        rows[n - 1].down = -1;
        Table table = new Table(rows, k, cmd);
        return table.doAllCmds();
    }

    public static void main(String[] args) {
        String[] cmd1 = {"D 2","C","U 3","C","D 4","C","U 2","Z","Z"};
        String[] cmd2 = {"D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"};

        Solution sol = new Solution();
        System.out.println(sol.solution(8, 2, cmd1));
        System.out.println(sol.solution(8, 2, cmd2));
    }
}
