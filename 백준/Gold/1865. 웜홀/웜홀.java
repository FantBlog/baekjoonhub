import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int test_case = Integer.parseInt(br.readLine()), A, B, now, Weight, N, M, W, now_weight, next, inf = 2147483647;
        StringTokenizer st;

        for (int tc = 0; tc < test_case; tc++) {
            ArrayList<ArrayList<Integer>> node = new ArrayList<>();

            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken()); // 노드 수
            M = Integer.parseInt(st.nextToken()); // 도로 수
            W = Integer.parseInt(st.nextToken()); // 웜홀 수

            for (int i = 0; i < N + 1; i++) {
                node.add(new ArrayList<>());
            }

            int[] dp = new int[N + 1];
            Arrays.fill(dp, inf);

            for (int i = 0; i < M; i++) {
                st = new StringTokenizer(br.readLine());
                A = Integer.parseInt(st.nextToken());
                B = Integer.parseInt(st.nextToken());
                Weight = Integer.parseInt(st.nextToken());
                node.get(A).add(B);
                node.get(A).add(Weight);
                node.get(B).add(A);
                node.get(B).add(Weight);
            }

            for (int i = 0; i < W; i++) {
                st = new StringTokenizer(br.readLine());
                A = Integer.parseInt(st.nextToken());
                B = Integer.parseInt(st.nextToken());
                Weight = -1 * Integer.parseInt(st.nextToken());
                node.get(A).add(B);
                node.get(A).add(Weight);
            }



            String result = "NO";
            for (int j = 0; j < N-1; j++) { // N-1번 반복
                for (now = 1; now <= N; now++) {
                    if (dp[now] == inf) dp[now] = 0; //dist[v] != INF인 모든 v에 대해

                    for (int i = 0; i < node.get(now).size(); i += 2) {
                        next = node.get(now).get(i);
                        now_weight = node.get(now).get(i + 1);

                        if (dp[next] > now_weight + dp[now]) {
                            dp[next] = now_weight + dp[now];
                        }
                    }
                }
            }
            // 음수 싸이클 검증을 위해 한바퀴 더 순회
            boolean breakpoint = false;
            for (now = 1; now <= N; now ++) {
                if (dp[now] == inf) continue; //dist[v] != INF인 모든 v에 대해

                for (int i = 0; i < node.get(now).size(); i += 2) {
                    next = node.get(now).get(i);
                    now_weight = node.get(now).get(i + 1);

                    if (dp[next] > now_weight + dp[now]){
                        result = "YES";
                        breakpoint = true;
                        break;
                    }
                }

                if (breakpoint) break;
            }

            bw.write(result + "\n");

        }
        bw.flush();

    }
}