import java.io.*;
import java.util.*;

public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        /*
		String st = new String(br.readLine());
		long N = Long.parseLong(br.readLine());
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
		st.nextToken();
        */
        int[][] ggong = new int[16][16];

        try {
            while (true){
                StringTokenizer st = new StringTokenizer(br.readLine());
                int Black = Integer.parseInt(st.nextToken());
                int White = Integer.parseInt(st.nextToken());

                for (int B = 15; B >= 0; B--){
                    for (int W = 15; W >= 0; W--) {
                        if (B > 0) ggong[B][W] = Math.max(ggong[B][W], ggong[B - 1][W] + Black);
                        if (W > 0) ggong[B][W] = Math.max(ggong[B][W], ggong[B][W - 1] + White);
                    }
                }
            }

        } catch (NullPointerException e) {
        }


        bw.write(ggong[15][15] + "");
        bw.flush();

    }
}