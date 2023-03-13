import java.io.*;
import java.util.*;


public class Main {
    public static long fac(long num, long sum) {
        return num == 1 ? sum : fac(num - 1, num * sum);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[][] arr = new int[26][200000];

        String st = new String(br.readLine());

        for (int i = 0; i < st.length(); i++) {
            arr[st.charAt(i) - 97][i] = arr[st.charAt(i) - 97][i] + 1;
            if (i != 0) {
                for (int j = 0; j < 26; j++) {
                    arr[j][i] = arr[j][i - 1] + arr[j][i];
                }
            }
        }
        int N = Integer.parseInt(br.readLine());
        int ch;
        int start;
        int end;
        for (int i = 0; i < N; i++) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            ch = (int) stk.nextToken().charAt(0);
            start = Integer.parseInt(stk.nextToken());
            end = Integer.parseInt(stk.nextToken());
            if (start != 0) bw.write(arr[ch - 97][end] - arr[ch - 97][start - 1] + "\n");
            else bw.write(arr[ch - 97][end] + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}