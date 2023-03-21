import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String text_1 = " " + br.readLine();
        String text_2 = " " + br.readLine();
        int N = text_1.length();
        int M = text_2.length();
        int[][] dp = new int[M][N];

        for (int j = 1; j < M; j++) {
            for (int i = 1; i < N; i++) {
                dp[j][i] = Math.max(dp[j][i-1],dp[j-1][i]);
                if (text_1.charAt(i) == text_2.charAt(j)) {
                    dp[j][i] = dp[j-1][i-1] + 1;
                }
            }
        }
        bw.write(dp[M-1][N-1] + "");
        bw.flush();
    }
}