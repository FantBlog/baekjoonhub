import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String st = br.readLine();
		
		int back, now, leng = st.length(), result = 1;
		int[][] dp = new int[leng][2];
		
		dp[0][0] = 1;

		back = Integer.parseInt(st.charAt(0)+"");
		if (back == 0) result = 0;
		for (int i = 1; i < leng; i++) {
			
			dp[i][0] = (dp[i-1][1] + dp[i-1][0]) % 1000000;
			now = Integer.parseInt(st.charAt(i)+"");
			
			if (0 < back && back < 3) {
				if (back == 2 && 7 > now) {
					dp[i][1] = dp[i-1][0] % 1000000;
				}
				if (back == 1) {
					dp[i][1] = dp[i-1][0] % 1000000;
				}
			}
			if (now == 0) {
				if (back == 1 || back == 2) {
                    back = now;
                    dp[i][0] = 0;
                    continue;
                }
				result = 0;
				break;
			}
			back = now;
		}
		if (result == 1) result = (dp[leng - 1][0] + dp[leng - 1][1]) % 1000000;
		System.out.println(result);
		
	}

}