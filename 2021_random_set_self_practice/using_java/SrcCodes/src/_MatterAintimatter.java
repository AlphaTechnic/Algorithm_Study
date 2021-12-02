/*
input :
7
2 5 -3 1 3 -4 4

output :
2
*/

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class _MatterAintimatter {
    static FastReader scan = new FastReader();
    static int N;
    static int[] arr;
    static ArrayList<Integer> cumSum;

    public static void input() {
        N = scan.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
        }
    }

    public static void makeCumSum() {
        cumSum = new ArrayList<>();
        cumSum.add(0);

        int tot = 0;
        for (int i = 0; i < N; i++) {
            tot += arr[i];
            cumSum.add(tot);
        }
    }

    public static long nC2(int n) {
        return ((long) n * (n - 1)) / 2;
    }

    public static void solution() {
        Collections.sort(cumSum);

        long tot = 0;
        int pre;
        int cnt = 1;
        for (int i = 1; i <= N; i++) {
            pre = cumSum.get(i - 1);
            int num = cumSum.get(i);
            if (num == pre) {
                cnt += 1;
                if (i == N && cnt >= 2) {
                    tot += nC2(cnt);
                }
            }
            else {
                if (cnt >= 2) {
                    tot += nC2(cnt);
                }
                cnt = 1;
            }
        }
        System.out.println(tot);
    }

    public static void main(String[] args) {
        _MatterAintimatter.input();
        _MatterAintimatter.makeCumSum();
        _MatterAintimatter.solution();
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
