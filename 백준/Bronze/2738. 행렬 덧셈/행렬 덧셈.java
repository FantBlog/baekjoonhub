import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int[][] arr = new int[R][C];

        for (int r = 0; r < R; r ++){
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < C; c++){
                arr[r][c] = Integer.parseInt(st.nextToken());
            }
        }
        for (int r = 0; r < R; r ++){
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < C; c++){
                arr[r][c] += Integer.parseInt(st.nextToken());
            }
        }

        for (int r = 0; r < R; r ++){
            for (int c = 0; c < C; c++){
                bw.write(arr[r][c]+" ");
            }
            bw.newLine();
        }

        bw.flush();
        br.close();
        bw.close();
    }
}