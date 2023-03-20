import java.io.*;
import java.util.*;

public class Main {
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int N;
    static int[] save;
    static int[][] arr;
    static int max = 0;
    static int result = 10000001;

    public static void backtracking(int deep, int idx) throws IOException {
        if (deep == N) {
            if (result > max){
                result = max;
            }
            return;
        }
        if (result < max) return;

        if (deep == N-1 && arr[idx][0] != 0){
            save[idx] = 1;
            max += arr[idx][0];

            backtracking(deep + 1, 0);

            max -= arr[idx][0];
            save[idx] = 0;
            return;
        }

        for (int i = 0; i < N; i++) {
            if (arr[idx][i] == 0 || save[i] > 0) continue;

            // idx = 시작지점 , i = 도착지점
            save[idx] = i + 1;
            max += arr[idx][i];

            backtracking(deep + 1, i);

            max -= arr[idx][i];
            save[idx] = 0;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        save = new int[N];

        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        backtracking(0,0);

        bw.write(result+"");
        bw.flush();
    }
}