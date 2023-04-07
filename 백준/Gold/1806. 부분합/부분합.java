import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int S = Integer.parseInt(st.nextToken());
				
		int[] nums = new int[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) nums[i] = Integer.parseInt(st.nextToken());
		
		int total = nums[0], max = N + 1, lp = 0, rp = 0;
		boolean result = true;
		while (lp < N) {
			if (total >= S && max > (rp - lp + 1)) {
				result = false;
				max = rp - lp + 1;
			}
			
			if (total < S && rp < N - 1) {
				total += nums[++rp];
			}
			else {
				total -= nums[lp++];
			}
			
		}
		
		if (result) System.out.println('0');
		else System.out.println(max);
		
		bw.flush();
	}
}
