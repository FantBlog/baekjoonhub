import java.util.*;
import java.io.*;

public class Main {
	static int[][] arr;
	static int[] dr = {0, 0, 1, -1}, dc = {1, -1, 0, 0};
	static int max, R, C;
	
	public static void back(int deep, int r, int c, int vis) {
		if (deep > max) max = deep;
		
		for (int i = 0; i < 4; i++) {
			int nr = r + dr[i], nc = c + dc[i];
			
			if (nr < 0 || R <= nr || nc < 0 || C <= nc) continue;
			
			if ((vis & (1 << arr[nr][nc])) > 0) continue;
			
			back(deep + 1, nr, nc, vis | (1 << arr[nr][nc]));
			
		}
	}
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		arr = new int[R][C];
		for (int i = 0; i < R; i++) {
			String temp = br.readLine();
			for (int j = 0; j < C; j++) {
				arr[i][j] = temp.charAt(j) - 65;
			}
		}
		max = 0;
		back(1, 0, 0, 1 << arr[0][0]);
		
		bw.write(max+"");
		bw.flush();
	}
}
