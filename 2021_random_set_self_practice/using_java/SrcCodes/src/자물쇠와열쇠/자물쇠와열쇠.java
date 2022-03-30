package 자물쇠와열쇠;


class Match {
    int[][] key;
    int[][] lock;
    int cntHole;
    int lockLength;
    int keyLength;

    // init
    public Match(int[][] key, int[][] lock) {
        this.key = key;
        this.keyLength = key.length;

        this.lockLength = lock.length;
        this.lock = new int[3 * this.lockLength][3 * this.lockLength];
        // init this.lock (3배 확대)
        this.cntHole = 0;
        for (int i = 0; i < 3 * this.lockLength; i++) {
            for (int j = 0; j < 3 * this.lockLength; j++) {
                this.lock[i][j] = -1;
            }
        }
        for (int i = 0; i < lock.length; i++) {
            for (int j = 0; j < lock.length; j++) {
                this.lock[i + this.lockLength][j + this.lockLength] = lock[i][j] ^ 1;
                if (lock[i][j] == 0) {  // hole 있는 부분
                    this.cntHole++;
                }
            }
        }
    }

    public boolean go() {
        int N = this.lockLength + this.keyLength;
        int move = this.lockLength - this.keyLength;

        int[][] keyRotated = this.key;
        for (int k = 0; k < 4; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    int sy = i + move;
                    int sx = j + move;
                    int[][] box = extract(sy, sx);
                    if (doMatch(box, keyRotated)) {
                        return true;
                    }
                }
            }
            keyRotated = this.rotate(keyRotated);
        }
        return false;
    }

    public int[][] extract(int sy, int sx) {
        int[][] ret = new int[this.keyLength][this.keyLength];
        for (int i = 0; i < this.keyLength; i++) {
            for (int j = 0; j < this.keyLength; j++) {
                ret[i][j] = this.lock[i + sy][j + sx];
            }
        }
        return ret;
    }

    public boolean doMatch(int[][] box, int[][] keyRotated) {
        int cnt = 0;
        for (int i = 0; i < this.keyLength; i++) {
            for (int j = 0; j < this.keyLength; j++) {
                if (box[i][j] == -1) {
                    continue;
                }

                if (box[i][j] != keyRotated[i][j]) {
                    return false;
                }
                if (box[i][j] == 1) {
                    cnt++;
                }
            }
        }

        return cnt == this.cntHole;
    }

    public int[][] rotate(int[][] org) {
        int N = org.length;
        int[][] ret = new int[N][N];
        for (int col = 0; col < N; col++) {
            for (int row = 0; row < N; row++) {
                ret[col][N - row - 1] = org[row][col];
            }
        }
        return ret;
    }
}


class Solution {
    public boolean solution(int[][] key, int[][] lock) {
        Match match = new Match(key, lock);
        return match.go();
    }

    public static void main(String[] args) {
        int[][] key = {{0, 0, 0}, {1, 0, 0}, {0, 1, 1}};
        int[][] lock = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
        Solution sol = new Solution();
        System.out.println(sol.solution(key, lock));
    }
}