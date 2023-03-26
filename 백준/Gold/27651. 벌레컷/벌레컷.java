import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine()), s, e, idx, center;
		long cnt = 0;
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		long[] arr = new long[N];
		
		arr[0] = Integer.parseInt(st.nextToken());
		
		for (int i = 1; i < N; i++) {
			arr[i] = arr[i - 1] + Long.parseLong(st.nextToken());
		}
		
		for (int i = N - 1; i > 1; i--) {
			
			s = 1;
			e = i - 1; 
			idx = 0;
			while (s <= e) {
				center = (s + e) >> 1;
		
				if (arr[center - 1] < arr[N - 1] - arr[i-1] && arr[N - 1] - arr[i-1] < arr[i - 1] - arr[center - 1]) {
					s = center + 1;
					idx = Math.max(idx, center);
				}
				else e = center - 1;
			}
			cnt += idx;
		}
		System.out.println(cnt);
	}

}