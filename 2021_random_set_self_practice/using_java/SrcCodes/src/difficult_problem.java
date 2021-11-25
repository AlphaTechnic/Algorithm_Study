import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class difficult_problem {

    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        if (N == 0) {
            System.out.println(1);
            return;
        }
        if (N == 1 || N == 2){
            System.out.println(N);
            return;
        }

        long n = 1;
        int p = 1;
        while (p <= N) {
            n = n * p;
            n = digitSum(n);
            p += 1;
        }
        System.out.println(n);
    }

    public static long digitSum(long n) {
        long tot = 0L;
        while (true) {
            String txt = String.valueOf(n);
            for (int i = 0; i < txt.length(); i++) {
                tot += (txt.charAt(i) - '0');
            }

            if (tot < 10) {
                break;
            }
            else {
                n = tot;
                tot = 0;
            }
        }
        return tot;
    }
}
