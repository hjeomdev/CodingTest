package avaj.BOJ.P11729;

import java.io.*;

public class Main {
    static int N;
    static StringBuilder sbd = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());

        int total = (int) Math.pow(2, N) - 1;
        System.out.println(total);

        hanoi(N, 1, 2, 3);

        System.out.print(sbd);
    }

    public static void hanoi(int n, int start, int mid, int to) {
        if (n == 1) {
            sbd.append(start).append(" ").append(to).append("\n");
            return;
        }

        hanoi(n - 1, start, to, mid); // n - 1개의 원반을 첫번째칸에서 두번째 칸으로 이동
        sbd.append(start).append(" ").append(to).append("\n");//hanoi(1, start, mid, to); // 1개의 원반을 첫번째에서 세번째 칸으로 이동
        hanoi(n - 1, mid, start, to); // n - 1개의 원반을 두번째칸에서 세번째 칸으로 이동
    }
}

// java.Math.pow(double a, double b)
// Doc: https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#pow-double-double-
// a의 b 승의 값을 반환하는 메소드