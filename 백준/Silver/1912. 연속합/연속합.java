import java.util.*;
import java.io.*;

class Main
{
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] dp = new int[N];
		int result = Integer.parseInt(st.nextToken());
		dp[0] = result;
		
		for (int i = 1; i < N; i++) {
			int now = Integer.parseInt(st.nextToken());
			
			dp[i] = Math.max(dp[i-1] + now, now);
			if (dp[i] > result) result = dp[i];
		}
		System.out.println(result);
	}
}