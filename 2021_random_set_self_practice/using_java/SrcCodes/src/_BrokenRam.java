/*
input :
3
256 274 512

output :
1
2
 */

import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class _BrokenRam {
    static _BrokenRam.FastReader scan = new _BrokenRam.FastReader();
    public static int[] arr;
    public static int N;

    public static void input() {
        N = scan.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
        }
    }

    public static boolean isValid(int num) {
        while (num != 1) {
            if ((num & 1) == 0) {
                num >>= 1;
            }
            else {
                return false;
            }
        }
        return true;
    }

    public static void detect() {
        int cnt = 0;
        ArrayList<Integer> ans = new ArrayList<Integer>();
        for (int i = 0; i < N; i++) {
            if (!(isValid(arr[i]))) {
                cnt++;
                ans.add(i + 1);
            }
        }
        System.out.println(cnt);
        for (Integer ele : ans) {
            System.out.printf("%d ", ele);
        }
        System.out.print("\n");
    }

    public static void main(String[] args) {
        _BrokenRam.input();
        _BrokenRam.detect();
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
