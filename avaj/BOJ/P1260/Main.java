package avaj.BOJ.P1260;

import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static StringBuilder sb = new StringBuilder();
    static int N, M, V;
    static int[][] matrix;
    static boolean[] visited;

    static Queue<Integer> q = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("BOJ/P1260/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        matrix = new int[N + 1][N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            matrix[a][b] = matrix[b][a] = 1;
        }

        dfs(V);
        sb.append("\n");

        visited = new boolean[N + 1];
        bfs(V);

        System.out.println(sb);
    }

    public static void dfs(int start) {
        visited[start] = true;
        sb.append(start + " ");

        for (int i = 0; i <= N; i++) {
            if (matrix[start][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int start) {
        q.add(start);
        visited[start] = true;

        while (!q.isEmpty()) {
            start = q.poll();
            sb.append(start + " ");

            for (int i = 1; i <= N; i++) {
                if (matrix[start][i] == 1 && !visited[i]) {
                    q.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}

// 여러 테스트 코드 한번에 돌리기
/*
package avaj.BOJ.P1260;

import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static int N, M, V;
    static int[][] matrix;
    static boolean[] visited;

    static BufferedReader br;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("BOJ/P1260/input.txt"));
        br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            init();
            dfs(V);
            sb.append("\n");

            visited = new boolean[N + 1];
            bfs(V);

            sb.append("\n\n");
        }

        System.out.println(sb);

    }

    public static void dfs(int start) {
        visited[start] = true;
        sb.append(start + " ");

        for (int i = 0; i <= N; i++) {
            if (matrix[start][i] == 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();

        q.add(start);
        visited[start] = true;


        while (!q.isEmpty()) {
            start = q.poll();
            sb.append(start + " ");

            for (int i = 1; i <= N; i++) {
                if (matrix[start][i] == 1 && !visited[i]) {
                    q.add(i);
                    visited[i] = true;
                }
            }
        }

    }

    public static void init() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        matrix = new int[N + 1][N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            matrix[a][b] = matrix[b][a] = 1;
        }
    }
}*/
