import java.util.LinkedList;
import java.util.Queue;

class Node {
    private final int y;
    private final int x;

    public Node(int y, int x) {
        this.y = y;
        this.x = x;
    }

    public int getY() {
        return this.y;
    }
    public int getX() {
        return this.x;
    }
}

class Graph {
    public static int[] dx = {1, 0, -1, 0};
    public static int[] dy = {0, 1, 0, -1};
    private final int[][] board;
    private final int R;
    private final int C;
    private final int[][] visited;
    Queue<Node> queue;

    public Graph(int[][] maps) {
        this.board = maps;
        this.R = maps.length;
        this.C = maps[0].length;
        this.visited = new int[this.R][this.C];
        this.queue = new LinkedList<>();
    }

    public int bfs() {
        this.queue.add(new Node(0, 0));
        this.visited[0][0] = 1;
        while (!queue.isEmpty()) {
            Node cur_node = queue.remove();
            int cy = cur_node.getY();
            int cx = cur_node.getX();
            if (cy == this.R - 1 && cx == this.C - 1) {
                break;
            }

            for (int i = 0; i < 4; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                if (ny < 0 || ny >= this.R) continue;
                if (nx < 0 || nx >= this.C) continue;
                if (this.board[ny][nx] == 0) continue;
                if (this.visited[ny][nx] > 0) continue;

                this.queue.add(new Node(ny, nx));
                this.visited[ny][nx] = this.visited[cy][cx] + 1;
            }
        }
        int ans = this.visited[this.R - 1][this.C - 1];
        if (ans != 0) {
            return ans;
        }
        return -1;
    }
}

class Solution {
    public int solution(int[][] maps) {
        Graph graph = new Graph(maps);
        return graph.bfs();
    }

    public static void main(String[] args) {
        int[][] maps = {{1,0,1,1,1},{1,0,1,0,1},{1,0,1,1,1},{1,1,1,0,1},{0,0,0,0,1}};
        Solution obj = new Solution();
        System.out.println(obj.solution(maps));
    }
}