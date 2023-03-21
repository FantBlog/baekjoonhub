import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] dp,line,visited;
    static int[][] arr;
    
    public static void DFS(int start){
        int max = 0;
        for (int i = 0; i < N;i++){
            if (arr[i][start] == 0) continue;

            if (visited[i] == 0) {
                visited[i] = 1;
                DFS(i);
            }
            if (max < dp[i]) max = dp[i];
        }
        dp[start] = max + line[start];
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken()); // 건물 개수
            int K = Integer.parseInt(st.nextToken()); // 연결 라인 수
            
            line = new int[N];
            visited = new int[N];
            dp = new int[N];
            arr = new int[N][N];
            int s, e, target;

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++){
                line[i] = Integer.parseInt(st.nextToken());
            }

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                s = Integer.parseInt(st.nextToken()) - 1;
                e = Integer.parseInt(st.nextToken()) - 1;
                arr[s][e] = 1;
            }

            target = Integer.parseInt(br.readLine()) - 1;
            visited[target] = 1;
            
            DFS(target);
            
            bw.write(dp[target]+"\n");

        }
        bw.flush();
    }
}