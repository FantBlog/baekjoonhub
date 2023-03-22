import java.io.*;
import java.util.*;
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine()), A, B, now;
        StringTokenizer st;

        ArrayList<ArrayList<Integer>> node = new ArrayList<>();
        for (int i = 0; i < N+1; i++) {
            node.add(new ArrayList<>());
        }
        int[] dp = new int[N+1];
        Queue<Integer> Q = new LinkedList<>();
        Q.add(1);
        dp[1] = 1;

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            A = Integer.parseInt(st.nextToken());
            B = Integer.parseInt(st.nextToken());
            node.get(A).add(B);
            node.get(B).add(A);
        }

        while (Q.size() > 0){
            now = Q.poll();
            for (int i = 0; i < node.get(now).size(); i++){
                if(node.get(now).get(i) > 0 && dp[node.get(now).get(i)] == 0){
                    dp[node.get(now).get(i)] = now;
                    Q.add(node.get(now).get(i));
                }
            }
        }
        for (int i = 2; i <= N; i++){
            bw.write(dp[i]+"\n");
        }
        bw.flush();

    }
}