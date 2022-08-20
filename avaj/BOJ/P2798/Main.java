package avaj.BOJ.P2798;

import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[] cards;
    static StringBuilder sbd = new StringBuilder();

    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("BOJ/P2798/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        cards = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        for (int i = 0; i < cards.length; i++) {
            for (int j = i + 1; j < cards.length; j++) {
                for (int k = j + 1; k < cards.length; k++) {
                    int sum = cards[i] + cards[j] + cards[k];
                    if (sum <= M){
                        answer = Math.max(answer, sum);
                    }
                }
            }
        }

        System.out.println(answer);
    }
}
