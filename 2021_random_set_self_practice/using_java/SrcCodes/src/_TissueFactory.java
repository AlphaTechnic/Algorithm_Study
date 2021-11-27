/*
input :
5 20
4 3 7 1 6

output :
8
 */
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class _TissueFactory {

    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();

        ArrayList<Integer> nums = new ArrayList<>();
        int mxv = -1;
        for (int i = 0; i < N; i++) {
            int num = sc.nextInt();
            nums.add(num);
            mxv = Math.max(mxv, num);
        }

        ArrayList<Integer> diff = new ArrayList<>();
        long diffTot = 0l;
        for (int i = 0; i < N; i++) {
            diffTot += mxv - nums.get(i);
            diff.add(mxv - nums.get(i));
        }
//        System.out.println(diff);
//        System.out.println(diffTot);

        long remain = M - diffTot;
        if (remain < 0) {
            System.out.println("No way!");
        }
        else {
            System.out.println(mxv + remain / N);
        }
    }
}
