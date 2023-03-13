import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = new int[1000001];
        arr[0] = 1;
        arr[1] = 1;
        int N = Integer.parseInt(br.readLine());
        if (N < 2) bw.write(arr[N]+"");
        else {
            for(int i = 2; i <= N; i++){
                arr[i] = (arr[i-1] + arr[i-2]) % 15746;
            }
            bw.write(arr[N]+"");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}