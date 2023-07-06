import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        long[][] nums = new long[N][N];
        long max_num = 0;

        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j <= i; j++) {
                int temp = Integer.parseInt(st.nextToken());
                nums[i][j] = temp;
                if(i == 0) max_num = temp;
            }
        }

        for(int i = 1; i < N; i++){
            for(int j = 0; j <= i; j++) {
                if(j == 0){
                    nums[i][j] += nums[i - 1][j];
                }
                else if(j == i){
                    nums[i][j] += nums[i - 1][j - 1];
                }
                else{
                    nums[i][j] += Math.max(nums[i - 1][j], nums[i - 1][j - 1]);
                }
                if(i == N-1){
                    max_num = Math.max(nums[i][j], max_num);
                }
            }
        }
        bw.write(max_num + "");
        bw.flush();

    }
}