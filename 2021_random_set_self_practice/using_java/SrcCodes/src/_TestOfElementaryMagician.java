import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class _TestOfElementaryMagician {

    public static class Info {
        public int y;
        public int x;
        public int remain;

        public Info(int y, int x, int remain) {
            this.y = y;
            this.x = x;
            this.remain = remain;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int [][] bd = new int[R][C];
        for (int r = 0; r < R; r++) {
            st = new StringTokenizer(br.readLine());
            String ln = st.nextToken();
            for (int c = 0; c < ln.length(); c++) {
                bd[r][c] = ln.charAt(c) - '0';
            }
        }
        System.out.println(bfs(bd, R, C, K / 10 ));
    }

    public static int bfs(int[][] bd, int R, int C, int remain) {
        Queue<Info> que = new LinkedList<>();
        Info info = new Info(0, 0, remain);
        que.add(info);

        int [][][] vis = new int[R][C][remain + 1];
        vis[0][0][remain] = 1;

        int [] dy = {0, 1, 0, -1};
        int [] dx = {1, 0, -1, 0};
        while (!que.isEmpty()) {
            Info cur = que.remove();
            if (cur.y == R - 1 && cur.x == C - 1) {
                return vis[cur.y][cur.x][cur.remain] - 1;
            }

            for (int i = 0; i < 4; i++) {
                int ny = cur.y + dy[i];
                int nx = cur.x + dx[i];
                if (!(0 <= ny && ny < R)) continue;
                if (!(0 <= nx && nx < C)) continue;

                if (bd[ny][nx] == 0 && vis[ny][nx][cur.remain] == 0) {
                    Info newInfo = new Info(ny, nx, cur.remain);
                    que.add(newInfo);
                    vis[ny][nx][cur.remain] = vis[cur.y][cur.x][cur.remain] + 1;
                }
                else if (bd[ny][nx] == 1) {
                    int nny = ny + dy[i];
                    int nnx = nx + dx[i];
                    if (!(0 <= nny && nny < R)) continue;
                    if (!(0 <= nnx && nnx < C)) continue;
                    if (bd[nny][nnx] == 1) continue;

                    if (cur.remain >= 1 && vis[nny][nnx][cur.remain - 1] == 0) {
                        Info newInfo = new Info(nny, nnx, cur.remain - 1);
                        que.add(newInfo);
                        vis[nny][nnx][cur.remain - 1] = vis[cur.y][cur.x][cur.remain] + 1;
                    }
                }
            }
        }
        return -1;
    }
}

