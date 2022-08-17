package BOJ.P10872;

import java.io.*;

public class Main {
    static int N;

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("BOJ/P10872/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        System.out.println(factorial(N));

    }

    public static int factorial(int n) {
        if (n <= 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
}
