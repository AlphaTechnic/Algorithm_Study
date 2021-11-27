/*
input :
30

output :
7
*/

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class TimeComplexity {

    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        System.out.println(countFive(N));
    }

    public static int countFive(int num) {
        int tot = 0;
        int numSave = num;
        int p = 5;
        while (p < numSave) {
            num = numSave;
            tot += num / p;
            p *= 5;
        }
        return tot;
    }
}