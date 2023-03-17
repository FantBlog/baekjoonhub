import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] X = new int[3];
        int[] Y = new int[3];
        for (int i = 0; i < 3; i++ ){
            StringTokenizer st = new StringTokenizer(br.readLine());
            X[i] = Integer.parseInt(st.nextToken());
            Y[i] = Integer.parseInt(st.nextToken());
        }

        int dx = X[1] - X[0];
        int dy = Y[1] - Y[0];

        int a = dy * (X[2] - X[0]);
        int b = dx * (Y[2] - Y[0]);

        if (a-b > 0) bw.write("-1");
        else if (a == b) bw.write("0");
        else bw.write("1");

        bw.flush();
        br.close();
        bw.close();
    }
}