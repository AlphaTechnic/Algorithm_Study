/*
input :
3
popooqoq
bvdobvd
banana

output :
Mirror
Mirror
Normal
 */
import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.StringTokenizer;

public class _MirrorWord {
    static _MirrorWord.FastReader scan = new _MirrorWord.FastReader();

    public static int N;
    public static HashMap<String, String> str2str;
    public static ArrayList<String> word;

    public static void input() {
        N = scan.nextInt();
        word = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String txt = scan.nextLine();
            word.add(i, txt);
        }
    }

    public static void init() {
        str2str = new HashMap<>();
        str2str.put("b", "d"); str2str.put("d", "b");
        str2str.put("i", "i");
        str2str.put("l", "l");
        str2str.put("m", "m");
        str2str.put("n", "n");
        str2str.put("o", "o");
        str2str.put("p", "q"); str2str.put("q", "p");
        str2str.put("s", "z"); str2str.put("z", "s");
        str2str.put("u", "u");
        str2str.put("v", "v");
        str2str.put("w", "w");
        str2str.put("x", "x");
    }

    public static void mirrorCheck(){
        for (int i = 0; i < N; i++) {
            int L = word.get(i).length();

            boolean fail_flag = false;
            for (int j = 0; j < L / 2 + 1; j++) {
                String ch = Character.toString(word.get(i).charAt(j));
                if (str2str.containsKey(ch)) {
                    String opposite = Character.toString(word.get(i).charAt(L - j - 1));
                    if (!str2str.get(ch).equals(opposite)) {
                        System.out.println("Normal");
                        fail_flag = true;
                        break;
                    }
                }
                else {
                    System.out.println("Normal");
                    fail_flag = true;
                    break;
                }
            }
            if (!fail_flag) {
                System.out.println("Mirror");
            }
        }
    }

    public static void main(String[] args) {
        _MirrorWord.input();
        _MirrorWord.init();
        _MirrorWord.mirrorCheck();
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
