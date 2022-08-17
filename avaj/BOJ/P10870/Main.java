package avaj.BOJ.P10870;

import java.io.*;

public class Main {
    static int N;

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("BOJ/P10870/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        System.out.println(fibonacci(N));
    }

    public static int fibonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        }
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
