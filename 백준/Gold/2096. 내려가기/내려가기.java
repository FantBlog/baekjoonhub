import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int mn, mx;
        int[][] arr = new int[N][3], dp = new int[N][3], dp2 = new int[N][3];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (i == 0) {
                    dp[i][j] = arr[i][j];
                    dp2[i][j] = arr[i][j];
                }
            }
        }
        for (int i = 1; i < N; i++) {
            for (int j = 0; j < 3; j++) {
                if (j == 0) {
                    if (dp[i - 1][j] > dp[i - 1][j + 1]) {
                        dp[i][j] = dp[i - 1][j] + arr[i][j];
                    }
                    else {
                        dp[i][j] = dp[i - 1][j + 1] + arr[i][j];
                    }
                    if (dp2[i - 1][j] > dp2[i - 1][j + 1]) {
                        dp2[i][j] = dp2[i - 1][j + 1] + arr[i][j];
                    }
                    else {
                        dp2[i][j] = dp2[i - 1][j] + arr[i][j];
                    }
                }

                if (j == 1) {
                    mx = dp[i-1][0];
                    mn = dp2[i-1][0];
                    for (int k = 1; k< 3; k++) {
                        if (mx < dp[i-1][k])
                            mx = dp[i-1][k];
                        if (mn > dp2[i-1][k])
                            mn = dp2[i-1][k];
                    }
                    dp[i][j] = mx + arr[i][j];
                    dp2[i][j] = mn + arr[i][j];
                }

                if (j == 2) {
                    if (dp[i - 1][j] > dp[i - 1][j - 1]) {
                        dp[i][j] = dp[i - 1][j] + arr[i][j];
                    }
                    else {
                        dp[i][j] = dp[i - 1][j - 1] + arr[i][j];
                    }
                    if (dp2[i - 1][j] > dp2[i - 1][j - 1]) {
                        dp2[i][j] = dp2[i - 1][j - 1] + arr[i][j];
                    }
                    else {
                        dp2[i][j] = dp2[i - 1][j] + arr[i][j];
                    }
                }
            }
        }

        mx = dp[N - 1][0];
        mn = dp2[N - 1][0];
        for (int j = 1; j < 3; j++) {
            if (mx < dp[N - 1][j])
                mx = dp[N - 1][j];
            if (mn > dp2[N - 1][j])
                mn = dp2[N - 1][j];
        }

        bw.write(mx + " " + mn);

        bw.flush();
        br.close();
        bw.close();
    }
}