import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class _Prisoner {
    static FastReader scan = new FastReader();
//    static StringBuilder sb = new StringBuilder();

    public static class Coordinate {
        public double x;
        public double y;

        public Coordinate(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    public static class Prisoner {
        public int N;
        public ArrayList<Coordinate> seq = new ArrayList<Coordinate>();

        public void input() {
            this.N = scan.nextInt();
            for (int i = 0; i < this.N; i++) {
                double a = scan.nextDouble();
                double b = scan.nextDouble();
                seq.add(i, new Coordinate(a, b));
            }
        }

        public int ccw(Coordinate p1, Coordinate p2, Coordinate p3) {
            double ret = (p2.x - p1.x) * (p3.y - p2.y) - (p2.y - p1.y) * (p3.x - p2.x);
            if (ret > 0) {
                return 1;
            } else if (ret < 0) {
                return -1;
            } else {
                return 0;
            }
        }

        public void go() {
            int idx = 0;
            while (idx != this.seq.size() - 2) {
                Coordinate p1 = this.seq.get(idx);
                Coordinate p2 = this.seq.get(idx + 1);
                Coordinate p3 = this.seq.get(idx + 2);
                int ret = ccw(p1, p2, p3);
                switch (ret) {
                    case 1:
                        System.out.println("LEFT");
                        break;
                    case -1:
                        System.out.println("RIGHT");
                        break;
                    default:
                        /* invalid fallthrough */
                        break;
                }
                idx++;
            }
        }
    }

    public static void main(String[] args) {
        Prisoner prisoner = new Prisoner();
        prisoner.input();
        prisoner.go();
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws FileNotFoundException {
            br = new BufferedReader(new FileReader(new File(s)));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}
