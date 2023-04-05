import java.util.*;
import java.io.*;

public class Main {
	static int[] nums;
	static int[][] tree;
    
	public static void merge_tree(int idx, int start, int end) {
		tree[idx] = new int[end - start + 1];
		if (start == end) {
			tree[idx][0] = nums[start];
			return;
		}
		
		int center = (start + end) >> 1;
		merge_tree(idx * 2, start, center);
		merge_tree(idx * 2 + 1, center + 1, end);
				
		int lp = 0, rp = 0, l_size = tree[idx * 2].length, r_size = tree[idx * 2 + 1].length, p = 0;
		while (lp < l_size && rp < r_size) {
			if (tree[idx * 2][lp] > tree[idx * 2 + 1][rp]) tree[idx][p++] = tree[idx * 2 + 1][rp++];
			else tree[idx][p++] = tree[idx * 2][lp++];
		}
		while (lp < l_size) tree[idx][p++] = tree[idx * 2][lp++];
		while (rp < r_size) tree[idx][p++] = tree[idx * 2 + 1][rp++];
	}
	
	public static int solution(int s, int e, int K, int idx, int start, int end){
		if (end < s || e < start) return 0;
		
		if (s <= start && end <= e) {
			int lp = 0, rp = tree[idx].length;
			int center;
			
			while (lp < rp) {
				center = (rp + lp) >> 1;
				if (tree[idx][center] <= K) lp = center + 1;
				else rp = center;
			}
			return rp;
		}
		
		int center = (start + end) >> 1;
		return solution(s, e, K, idx * 2, start, center) + solution(s, e, K, idx * 2 + 1, center + 1, end);
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		nums = new int[N + 1];
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) nums[i] = Integer.parseInt(st.nextToken());
		
		int val = 2;
		while (true) {
			if (val >= N) {
				tree = new int[val << 1][];
				break;
			}
			val = val << 1;
		}
		
		merge_tree(1, 1, N);
		
		int s = 0, e = 0, K = 0, l = 0, r = 0, center = 0;
		for (int order = 0; order < M; order++) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken()); // 시작 인덱스 1시작
			e = Integer.parseInt(st.nextToken()); // 끝 인덱스
			K = Integer.parseInt(st.nextToken()); // K번째 수
			
			l = -(int)1e9;
			r = (int)1e9;
			while (l <= r) {
				center = (l + r) >> 1;
				if (solution(s, e, center, 1, 1, N) > K - 1) r = center - 1;
				else l = center + 1;
			}
			bw.write(l + "\n");
		}
		bw.flush();
	}
}
