import java.io.*;
import java.util.*;

public class Main {
    public static long sum(long[] arr) {
        long total = 0;
        for (int i = 0; i < arr.length; i++){
            total = total + arr[i];
        }
        return total;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        long[][] arr = new long[101][10];
        for (int i = 1; i < 10; i++) {
            arr[1][i] = 1;
        }

        int N = Integer.parseInt(br.readLine());
        if (N ==1 ) bw.write(sum(arr[N])+"");
        else {
            for (int i = 2; i <= N; i++) {
                arr[i][0] = arr[i-1][1];
                for (int j = 1; j < 9; j++) {
                    arr[i][j] = (arr[i-1][j-1] + arr[i-1][j+1]) % 1000000000;
                }
                arr[i][9] = arr[i-1][8];
            }
            bw.write(sum(arr[N]) % 1000000000 + "");
        }
        bw.flush();
        br.close();
        bw.close();
    }
}