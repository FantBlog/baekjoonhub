import java.util.*;
import java.io.*;

public class Main {
	static int[] tree, nums;
	static final int MAX = 65537;
    
	public static void update(int num, int diff, int idx, int start, int end) {
		if (end < num || num < start) return;
		tree[idx] += diff;
		
		if (start == end) return;
		
		int center = (start + end) >> 1;
		update(num, diff, idx * 2, start, center);
		update(num, diff, idx * 2 + 1, center + 1, end);
	}
	
	public static int cal(int idx, int num, int start, int end) {
		if (start == end) return start;
		
		int center = (start + end) >> 1;
		if (tree[idx * 2] >= num) return cal(idx * 2, num, start, center);
		else return cal(idx * 2 + 1, num - tree[idx * 2], center + 1, end);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		tree = new int[MAX * 4];
		nums = new int[N + 1];
		
		long total = 0;
		
		for (int i = 1; i <= N; i++) {
			nums[i] = Integer.parseInt(br.readLine());
			update(nums[i], 1, 1, 0, MAX);
			if (i >= K) {
				total += cal(1, (K + 1) >> 1, 0, MAX);
				update(nums[i - K + 1], -1, 1, 0, MAX);
			}
		}
		System.out.println(total);
	}
}
