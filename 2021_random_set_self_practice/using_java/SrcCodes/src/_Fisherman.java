/*
input :
5 10
5 3 7 2 1

output :
2
 */

import java.io.*;
import java.util.StringTokenizer;

public class _Fisherman {

    static _Fisherman.FastReader scan = new _Fisherman.FastReader();
    public static int N, K;
    public static int[] arr;
    public static int[] cumSum;

    public static void input() {
        N = scan.nextInt();
        K = scan.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
        }
    }

    public static void makeCumulativeSum() {
        cumSum = new int [N + 1];

        int tot = 0;
        for (int i = 0; i < N; i++) {
            tot += arr[i];
            cumSum[i + 1] = tot;
        }
    }

    public static void twoPointer() {
        int l = 0;
        int r = 0;
        int intervalSum;
        int cnt = 0;
        while (r != N + 1) {
            intervalSum = cumSum[r] - cumSum[l];
            if (intervalSum > K) {
                l++;
            }
            else if (intervalSum == K) {
                cnt++;
                r++;
            }
            else if (intervalSum < K) {
                r++;
            }
        }
        System.out.println(cnt);
    }


    public static void main(String[] args) {
        _Fisherman.input();
        _Fisherman.makeCumulativeSum();
        _Fisherman.twoPointer();
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
