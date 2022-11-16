package avaj.BOJ.P2178;

// 2022. 11. 17
// 17740KB	212ms
// 현재 루트보다 많이 헤매면서 방문한 곳이라면 다시 방문할 필요가 있지만, 똑같은 수준으로 헤맸다면 다시 방문할 필요가 없다.
// 큐 대신에 2차원 배열과 현재 탐색 중인 곳 인덱스와 추가할 위치 인덱스를 가지고 구현하면 좀더 빨리 처리할 수 있다.

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        System.setIn(new FileInputStream("BOJ/P2178/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] maze = new int[N][];
        for (int i = 0; i < N; i++) {
            maze[i] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
        }

        System.out.println(bfs(0, 0, maze));

    }

    public static int bfs(int x, int y, int[][] maze) {
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, -1, 0, 1};

        int[][] visited = new int[maze.length][maze[0].length];

        Queue<int[]> q = new LinkedList<>();

        q.add(new int[]{x, y, 1});
        visited[x][y] = 1;

        while (!q.isEmpty()) {
            int[] current = q.remove();
            for (int i = 0; i < dx.length; i++) {
                int[] move = {current[0] + dx[i], current[1] + dy[i], current[2] + 1}; // new_X, new_Y, new_cnt

                if (move[0] < 0 || move[0] > maze.length - 1 || move[1] < 0 || move[1] > maze[0].length - 1) {
                    continue;
                }

                if (maze[move[0]][move[1]] == 1 && (visited[move[0]][move[1]] == 0 || visited[move[0]][move[1]] > move[2])) {
                    q.add(move);
                    visited[move[0]][move[1]] = move[2];
                }

            }
        }

        return visited[visited.length - 1][visited[0].length - 1];
    }
}
